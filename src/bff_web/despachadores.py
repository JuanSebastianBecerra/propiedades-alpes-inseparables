import pulsar
from pulsar.schema import *
#from .eventos import *
from .comandos  import *

from . import utils

class Despachador:
    def __init__(self):
        ...

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoCrearPropiedad))
        publicador.send(mensaje)
        cliente.close()



    def publicar_comando(self, comando, topico):
        payload = ComandoCreaPropiedadPayload(
            id_propiedad = str(comando.id_propiedad),
            nombre_propiedad = str(comando.nombre_propiedad),
            estado_propiedad = str(comando.estado_propiedad),
            cliente_propiedad = str(comando.cliente_propiedad)
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))
        print(f"===================== Comando publicado en [{topico}] =====================")



 