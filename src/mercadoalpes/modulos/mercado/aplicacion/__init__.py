from pydispatch import dispatcher

from .handlers import HandlerTransaccionIntegracion

from src.mercadoalpes.modulos.mercado.dominio.eventos import TransaccionCreada

dispatcher.connect(HandlerTransaccionIntegracion.handle_transaccion_creada, signal=f'{TransaccionCreada.__name__}Integracion')