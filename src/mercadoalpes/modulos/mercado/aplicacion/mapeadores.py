from .dto import TransaccionDTO, SagalogDTO
from src.mercadoalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from src.mercadoalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from src.mercadoalpes.modulos.mercado.dominio.entidades import Transaccion, Sagalog

from datetime import datetime


class MapeadorTransaccionDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> TransaccionDTO:
        transaccion_dto = TransaccionDTO(id_propiedad=externo.get("id_propiedad"),
                                         tipo_transaccion=externo.get("tipo_transaccion"))
        return transaccion_dto

    def dto_a_externo(self, dto: TransaccionDTO) -> dict:
        return dto.__dict__


class MapeadorTransaccion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Transaccion.__class__

    def obtener_clase(self) -> type:
        return Transaccion

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        id_propiedad = str(entidad.id_propiedad)
        tipo_transaccion = entidad.tipo_transaccion

        return TransaccionDTO(fecha_creacion, fecha_actualizacion, _id, id_propiedad, tipo_transaccion)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion()
        transaccion.id_propiedad = dto.id_propiedad
        transaccion.tipo_transaccion = dto.tipo_transaccion
        return transaccion


class MapeadorSagalogDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> SagalogDTO:
        sagalog_dto = SagalogDTO(mensaje=externo.get("mensaje"), tipo_evento=externo.get("tipo_evento")
                                 , index_paso=externo.get("index_paso"),
                                 siguiente_accion=externo.get("siguiente_accion"))
        return sagalog_dto

    def dto_a_externo(self, dto: SagalogDTO) -> dict:
        return dto.__dict__


class MapeadorSagalog(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Sagalog.__class__

    def obtener_clase(self) -> type:
        return Sagalog

    def entidad_a_dto(self, entidad: Sagalog) -> SagalogDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        mensaje = str(entidad.mensaje)
        tipo_evento = entidad.tipo_evento
        index_paso = entidad.index_paso
        siguiente_accion = entidad.siguiente_accion

        return SagalogDTO(fecha_creacion, fecha_actualizacion, _id, mensaje, tipo_evento, index_paso, siguiente_accion)

    def dto_a_entidad(self, dto: SagalogDTO) -> Sagalog:
        sagalog = Sagalog()
        sagalog.mensaje = dto.mensaje
        sagalog.tipo_evento = dto.tipo_evento
        sagalog.index_paso = dto.index_paso
        sagalog.siguiente_accion = dto.siguiente_accion
        return sagalog
