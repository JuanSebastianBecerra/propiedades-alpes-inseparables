import uuid
from dataclasses import dataclass
from src.mercadoalpes.seedwork.dominio.eventos import EventoDominio

class EventoPropiedad(EventoDominio):
    ...

@dataclass
class EstadoPropiedadCambiado(EventoPropiedad):
    id_propiedad: str = None
    tipo_transaccion: str = None

@dataclass
class CambioEstadoFallido(EventoPropiedad):
    id_propiedad: str = None
    tipo_transaccion: str = None

@dataclass
class ConfirmacionCambioEstadoRevertido(EventoPropiedad):
    id_propiedad: str = None
    tipo_transaccion: str = None

    def __init__(self):
        print("ejecute la confirmacion de estado")