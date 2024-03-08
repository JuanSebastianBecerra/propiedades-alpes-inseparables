from pulsar.schema import *
from dataclasses import dataclass, field
from .comandosIntegracion import *

class ComandoCrearClientePayload(ComandoIntegracion):
    id_cliente = String()

class ComandoCrearCliente(ComandoIntegracion):
    data = ComandoCrearClientePayload()

class ComandoCreaPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()
    nombre_propiedad = String()
    estado_propiedad = String()
    cliente_propiedad = String()


class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCreaPropiedadPayload()