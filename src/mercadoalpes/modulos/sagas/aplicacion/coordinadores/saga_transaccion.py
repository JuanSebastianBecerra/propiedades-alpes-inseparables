from src.mercadoalpes.modulos.mercado.aplicacion.comandos.crear_transaccion import CrearTransaccion
from src.mercadoalpes.modulos.mercado.dominio.eventos.transacciones import CancelarTransaccion, \
    CreacionTransaccionFallida, TransaccionCreada
from src.mercadoalpes.modulos.sagas.aplicacion.comandos.propiedades import CambiarEstadoPropiedad
from src.mercadoalpes.modulos.sagas.dominio.eventos.propiedades import EstadoPropiedadCambiado, CambioEstadoFallido, \
    ConfirmacionCambioEstadoRevertido
from src.mercadoalpes.seedwork.aplicacion.comandos import Comando
from src.mercadoalpes.seedwork.aplicacion.sagas import Transaccion, CoordinadorOrquestacion, Inicio, Fin
from src.mercadoalpes.seedwork.dominio.eventos import EventoDominio
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

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...

    def construir_comando_prueba(self, comando: Comando):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        if comando == CrearTransaccion:
            comando = CrearTransaccion(fecha_creacion="", fecha_actualizacion="", id="", id_propiedad="",
                                       tipo_transaccion="")
        elif comando == CambiarEstadoPropiedad:
            comando = CambiarEstadoPropiedad()
        if comando is not None:
            comando.health()
            print("pase por aca")


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    print(mensaje)
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorTransacciones()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")

def oir_mensaje_prueba():
    coordinador = CoordinadorTransacciones()
    coordinador.set_pasos(coordinador.inicializar_pasos())
    coordinador.procesar_evento_prueba()