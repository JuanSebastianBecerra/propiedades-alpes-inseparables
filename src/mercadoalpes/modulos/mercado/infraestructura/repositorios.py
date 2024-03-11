from src.mercadoalpes.config.db import db
from src.mercadoalpes.modulos.mercado.dominio.repositorios import RepositorioTransacciones
from src.mercadoalpes.modulos.mercado.dominio.entidades import Transaccion, Sagalog
from src.mercadoalpes.modulos.mercado.dominio.fabricas import FabricaHistorico
from .dto import Transaccion as TransaccionDTO
from .dto import Sagalog as SagalogDTO
from .mapeadores import MapeadorTransaccion, MapeadorSagalog
from uuid import UUID



class RepositorioTransaccionesSQLite(RepositorioTransacciones):

    def __init__(self):
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos

    def obtener_por_id(self, id: UUID) -> Transaccion:
        transaccion_dto = db.session.query(TransaccionDTO).filter_by(id=str(id)).one()
        return self.fabrica_historicos.crear_objeto(transaccion_dto, MapeadorTransaccion())

    def obtener_todos(self) -> list[Transaccion]:
        list_transaccion_dto = db.session.query(TransaccionDTO)
        list_transaction: list[Transaccion] = list(map(lambda transaccion_dto: self.fabrica_historicos.crear_objeto(transaccion_dto, MapeadorTransaccion()), list_transaccion_dto))
        return list_transaction

    def agregar(self, transaccion: Transaccion):
        transaccion_dto = self.fabrica_historicos.crear_objeto(transaccion, MapeadorTransaccion())
        db.session.add(transaccion_dto)
        db.session.commit()

    def actualizar(self, transaccion: Transaccion):
        # TODO
        raise NotImplementedError

    def eliminar(self, transaccion_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioSagalogSQLite(RepositorioTransacciones):

    def __init__(self):
        self._fabrica_historicos: FabricaHistorico = FabricaHistorico()

    @property
    def fabrica_historicos(self):
        return self._fabrica_historicos

    def obtener_por_id(self, id: UUID) -> Sagalog:
        sagalog_dto = db.session.query(SagalogDTO).filter_by(id=str(id)).one()
        return self.fabrica_historicos.crear_objeto(sagalog_dto, MapeadorSagalog())

    def obtener_todos(self) -> list[Sagalog]:
        list_sagalog_dto = db.session.query(SagalogDTO)
        list_sagalog: list[Sagalog] = list(map(lambda sagalog_dto: self.fabrica_historicos.crear_objeto(sagalog_dto, MapeadorTransaccion()), list_sagalog_dto))
        return list_sagalog

    def agregar(self, sagalog: Sagalog):
        sagalog_dto = self.fabrica_historicos.crear_objeto(sagalog, MapeadorSagalog())
        db.session.add(sagalog_dto)
        db.session.commit()

    def actualizar(self, transaccion: Transaccion):
        # TODO
        raise NotImplementedError

    def eliminar(self, transaccion_id: UUID):
        # TODO
        raise NotImplementedError