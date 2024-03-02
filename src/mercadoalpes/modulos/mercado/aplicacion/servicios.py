from typing import Dict, Any

from src.mercadoalpes.seedwork.aplicacion.servicios import Servicio
from src.mercadoalpes.modulos.mercado.infraestructura.fabricas import FabricaRepositorio
from src.mercadoalpes.modulos.mercado.dominio.repositorios import RepositorioTransacciones
from src.mercadoalpes.modulos.mercado.dominio.fabricas import FabricaHistorico
from src.mercadoalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .dto import TransaccionDTO


from .mapeadores import MapeadorTransaccion
from ..dominio.entidades import Transaccion


class ServicioTransaccion(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos

    def crear_transaccion(self, transaccion_dto: TransaccionDTO) -> TransaccionDTO:
        mapeador_transaccion = MapeadorTransaccion()
        transaccion: Transaccion = self.fabrica_historicos.crear_objeto(transaccion_dto, mapeador_transaccion)
        transaccion.crear_transaccion(transaccion=transaccion)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, transaccion)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_historicos.crear_objeto(transaccion, mapeador_transaccion)

    def obtener_transaccion_por_id(self, id) -> TransaccionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        return repositorio.obtener_por_id(id).__dict__

    def obtener_todos(self) -> list[TransaccionDTO]:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        return repositorio.obtener_todos()