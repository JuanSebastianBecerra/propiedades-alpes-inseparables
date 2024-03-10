from src.mercadoalpes.modulos.mercado.dominio.entidades import Transaccion, Sagalog
from src.mercadoalpes.seedwork.dominio.repositorios import Mapeador
from .dto import Transaccion as TransaccionDTO
from .dto import Sagalog as SagalogDTO


class MapeadorTransaccion(Mapeador):

    def obtener_tipo(self) -> type:
        return Transaccion.__class__

    def obtener_clase(self) -> type:
        return Transaccion

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        
        transaccion_dto = TransaccionDTO()
        transaccion_dto.fecha_creacion = entidad.fecha_creacion
        transaccion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        transaccion_dto.id = str(entidad.id)
        transaccion_dto.id_propiedad = str(entidad.id_propiedad)
        transaccion_dto.tipo_transaccion = entidad.tipo_transaccion

        return transaccion_dto

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion(dto.id, dto.fecha_creacion, dto.fecha_actualizacion, dto.id_propiedad,dto.tipo_transaccion)
        transaccion.id_propiedad = dto.id_propiedad
        transaccion.tipo_transaccion=dto.tipo_transaccion
        return transaccion


class MapeadorSagalog(Mapeador):

    def obtener_tipo(self) -> type:
        return Sagalog.__class__

    def obtener_clase(self) -> type:
        return Sagalog

    def entidad_a_dto(self, entidad: Sagalog) -> SagalogDTO:
        sagalog_dto = SagalogDTO()
        sagalog_dto.fecha_creacion = entidad.fecha_creacion
        sagalog_dto.fecha_actualizacion = entidad.fecha_actualizacion
        sagalog_dto.id = str(entidad.id)
        sagalog_dto.mensaje = str(entidad.mensaje)
        sagalog_dto.tipo_evento = entidad.tipo_evento
        sagalog_dto.index_paso = entidad.index_paso
        sagalog_dto.siguiente_accion = entidad.siguiente_accion

        return sagalog_dto

    def dto_a_entidad(self, dto: SagalogDTO) -> Sagalog:
        sagalog = Sagalog(str(dto.id), dto.fecha_creacion, dto.fecha_actualizacion, dto.mensaje,
                                  dto.tipo_evento, dto.index_paso, dto.siguiente_accion)
        sagalog.mensaje = dto.mensaje
        sagalog.tipo_evento = dto.tipo_evento
        sagalog.index_paso = dto.index_paso
        sagalog.siguiente_accion = dto.siguiente_accion
        return sagalog