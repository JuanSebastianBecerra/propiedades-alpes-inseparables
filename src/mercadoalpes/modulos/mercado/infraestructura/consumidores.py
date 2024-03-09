import pulsar,_pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.eventos import EventoTransaccionCreada
from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.comandos import ComandoCrearTransaccion
from src.mercadoalpes.modulos.sagas.aplicacion.coordinadores.saga_transaccion import oir_mensaje
from src.mercadoalpes.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-transaccion', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-eventos',
                                       schema=AvroSchema(EventoTransaccionCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            oir_mensaje(mensaje)
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-transaccion', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-comandos',
                                       schema=AvroSchema(ComandoCrearTransaccion))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()