from pulsar.schema import *
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearTransaccionPayload(ComandoIntegracion):
    id_usuario = String()


class ComandoCrearTransaccion(ComandoIntegracion):
    data = ComandoCrearTransaccionPayload()