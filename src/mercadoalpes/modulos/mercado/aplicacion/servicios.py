from typing import Dict, Any

from src.mercadoalpes.seedwork.aplicacion.servicios import Servicio
from src.mercadoalpes.modulos.mercado.infraestructura.fabricas import FabricaRepositorio
from src.mercadoalpes.modulos.mercado.dominio.repositorios import RepositorioTransacciones, RepositorioSagalog
from src.mercadoalpes.modulos.mercado.dominio.fabricas import FabricaHistorico
from .dto import TransaccionDTO, SagalogDTO

from .mapeadores import MapeadorTransaccion, MapeadorSagalog
from ..dominio.entidades import Transaccion, Sagalog


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

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        repositorio.agregar(transaccion)

        return self.fabrica_historicos.crear_objeto(transaccion, mapeador_transaccion)

    def obtener_transaccion_por_id(self, id) -> TransaccionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        return repositorio.obtener_por_id(id).__dict__

    def obtener_todos(self) -> list[TransaccionDTO]:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        return repositorio.obtener_todos()


class ServicioSagalog(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos

    def crear_sagalog(self, sagalog_dto: SagalogDTO) -> SagalogDTO:
        mapeador_sagalog = MapeadorSagalog()
        sagalog: Sagalog = self.fabrica_historicos.crear_objeto(sagalog_dto, mapeador_sagalog)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagalog)
        repositorio.agregar(sagalog)

        return self.fabrica_historicos.crear_objeto(sagalog, mapeador_sagalog)