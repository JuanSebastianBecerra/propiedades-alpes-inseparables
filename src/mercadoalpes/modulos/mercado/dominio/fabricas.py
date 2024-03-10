from .entidades import Transaccion, Sagalog
from .reglas import TienePropiedad

from .excepciones import TipoObjetoNoExisteEnDominioMercadoExcepcion
from src.mercadoalpes.seedwork.dominio.repositorios import Mapeador
from src.mercadoalpes.seedwork.dominio.fabricas import Fabrica
from src.mercadoalpes.seedwork.dominio.entidades import Entidad

from dataclasses import dataclass

@dataclass
class FabricaTransaccion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            transaccion: Transaccion = mapeador.dto_a_entidad(obj)
            self.validar_regla(TienePropiedad(transaccion.id_propiedad))
            
            return transaccion


@dataclass
class FabricaSagalog(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            sagalog: Sagalog = mapeador.dto_a_entidad(obj)

            return sagalog

@dataclass
class FabricaHistorico(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_clase() == Transaccion:
            fabrica_transaccion = FabricaTransaccion()
            return fabrica_transaccion.crear_objeto(obj, mapeador)
        elif mapeador.obtener_clase() == Sagalog:
            fabrica_sagalog = FabricaSagalog()
            return fabrica_sagalog.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioMercadoExcepcion()