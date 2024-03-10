from src.mercadoalpes.seedwork.aplicacion.handlers import Handler
from src.mercadoalpes.modulos.mercado.infraestructura.despachadores import Despachador

class HandlerTransaccionIntegracion(Handler):

    @staticmethod
    def handle_transaccion_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-mercado')


    