from src.mercadoalpes.modulos.mercado.aplicacion.comandos.crear_transaccion import CrearTransaccion
from src.mercadoalpes.modulos.mercado.dominio.eventos.transacciones import CancelarTransaccion, \
    CreacionTransaccionFallida, TransaccionCreada
from src.mercadoalpes.modulos.sagas.aplicacion.comandos.propiedades import CambiarEstadoPropiedad
from src.mercadoalpes.modulos.sagas.dominio.eventos.propiedades import EstadoPropiedadCambiado, CambioEstadoFallido, \
    ConfirmacionCambioEstadoRevertido
from src.mercadoalpes.seedwork.aplicacion.comandos import Comando
from src.mercadoalpes.seedwork.aplicacion.sagas import Transaccion, CoordinadorOrquestacion, Inicio, Fin
from src.mercadoalpes.seedwork.dominio.eventos import EventoDominio
from src.mercadoalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.eventos import EventoTransaccionCreada, EventoTransaccionCreadaPayload


class CoordinadorTransacciones(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearTransaccion, evento=EventoTransaccionCreada, error=CreacionTransaccionFallida,
                        compensacion=CancelarTransaccion),
            Transaccion(index=2, comando=CambiarEstadoPropiedad, evento=EstadoPropiedadCambiado, error=CambioEstadoFallido,
                        compensacion=ConfirmacionCambioEstadoRevertido),
            Fin()
        ]
        return self.pasos

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])

    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje, index_paso, evento, next_step):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self,mensaje, evento: EventoDominio, tipo_comando: type):
        comando = Comando()
        if type(evento) == type(EventoTransaccionCreada) and type(tipo_comando) == type(CambiarEstadoPropiedad):
            comando = CambiarEstadoPropiedad()
        return comando


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje, event_class):
    if type(event_class) == type(EventoDominio) or type(event_class) == type(EventoIntegracion):
        coordinador = CoordinadorTransacciones()
        coordinador.set_pasos(coordinador.inicializar_pasos())
        coordinador.procesar_evento(mensaje, event_class)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")