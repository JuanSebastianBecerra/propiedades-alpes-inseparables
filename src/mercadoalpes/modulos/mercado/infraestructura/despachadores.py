import pulsar
from pulsar.schema import *

from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.eventos import EventoTransaccionCreada, EventoTransaccionCreadaPayload
from src.mercadoalpes.modulos.mercado.infraestructura.schema.v1.comandos import ComandoCrearTransaccion, ComandoCrearTransaccionPayload
from src.mercadoalpes.seedwork.infraestructura import utils

import datetime, pika, json

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

# class Despachador:
    # def _publicar_mensaje(self, mensaje, topico):
    #     connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    #     channel = connection.channel()
    #     channel.queue_declare(queue=topico)
    #     channel.basic_publish(exchange='',
    #                             routing_key=topico,
    #                             body=json.dumps(mensaje))
    #     print("========== Mensaje publicado ==========", flush=True)
    #     connection.close()
    #
    # def publicar_evento(self, evento, topico):
    #     payload = EventoTransaccionCreadaPayload(
    #         id_propiedad=str(evento.id_propiedad),
    #         fecha_creacion=int(unix_time_millis(evento.fecha_evento))
    #     )
    #     evento_integracion = EventoTransaccionCreada(data=payload)
    #     self._publicar_mensaje(evento_integracion.toJSON(), topico)
    # def _publicar_mensaje(self, mensaje, topico, schema):
    #     cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
    #     publicador = cliente.create_producer(topico, schema=AvroSchema(EventoTransaccionCreada))
    #     publicador.send(mensaje)
    #     cliente.close()
    #
    # def publicar_evento(self, evento, topico):
    #     # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
    #     payload = EventoTransaccionCreadaPayload(
    #         id_reserva=str(evento.id_reserva),
    #         id_cliente=str(evento.id_cliente),
    #         estado=str(evento.estado),
    #         fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
    #     )
    #     evento_integracion = EventoTransaccionCreada(data=payload)
    #     self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoTransaccionCreada))
    #
    # def publicar_comando(self, comando, topico):
    #     # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
    #     payload = ComandoCrearTransaccionPayload(
    #         id_usuario=str(comando.id_usuario)
    #         # agregar itinerarios
    #     )
    #     comando_integracion = ComandoCrearTransaccion(data=payload)
    #     self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearTransaccion))
class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoTransaccionCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        print("publique el evento")
        print(evento)
        payload = EventoTransaccionCreadaPayload(
            id_propiedad=str(evento.id_propiedad),
        )
        evento_integracion = EventoTransaccionCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoTransaccionCreada))

    def publicar_comando(self, comando, topico):
        print("publique el comando")
        print(comando)
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearTransaccionPayload(
            id_propiedad=str(comando.id_propiedad)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearTransaccion(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearTransaccion))