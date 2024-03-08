from pulsar.schema import *

import json
from src.bff_web.mensajes import *
from src.bff_web.eventointegracion import *

class EventoTransaccionCreadaPayload(Record):
    id_propiedad = String()
    fecha_creacion = Long()
    tipo_transaccion = String()

class EventoTransaccionCreada(EventoIntegracion):
    data = EventoTransaccionCreadaPayload()

class EventoIntegracion(Mensaje):
    ...