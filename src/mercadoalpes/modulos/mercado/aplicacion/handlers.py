from src.mercadoalpes.seedwork.aplicacion.handlers import Handler
from src.mercadoalpes.modulos.mercado.infraestructura.despachadores import Despachador

from src.mercadoalpes.modulos.sagas.aplicacion.coordinadores.saga_transaccion import CoordinadorTransacciones, oir_mensaje_prueba

class HandlerTransaccionIntegracion(Handler):

    @staticmethod
    def handle_transaccion_creada():
        oir_mensaje_prueba()
        # despachador = Despachador()
        # despachador.publicar_evento(evento, 'eventos-mercado')


    