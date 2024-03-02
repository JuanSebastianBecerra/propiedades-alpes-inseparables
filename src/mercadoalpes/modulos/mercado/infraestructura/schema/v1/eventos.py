from pulsar.schema import *
from src.mercadoalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
import json

class EventoTransaccionCreadaPayload(Record):
    id_propiedad = String()

class EventoTransaccionCreada(EventoIntegracion):
    data = EventoTransaccionCreadaPayload()

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #         sort_keys=True, indent=4)