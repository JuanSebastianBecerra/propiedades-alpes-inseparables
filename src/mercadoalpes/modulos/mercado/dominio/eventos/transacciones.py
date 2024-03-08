from __future__ import annotations
from dataclasses import dataclass, field
from src.mercadoalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoTransaccion(EventoDominio):
    ...

@dataclass
class TransaccionCreada(EventoTransaccion):
    id_propiedad: str = None
    fecha_creacion: datetime = None
    tipo_transaccion: str = None

@dataclass
class CreacionTransaccionFallida(EventoTransaccion):
    id_propiedad: str = None
    fecha_creacion: datetime = None
    tipo_transaccion: str = None

@dataclass
class CancelarTransaccion(EventoTransaccion):
    id_propiedad: str = None
    fecha_creacion: datetime = None
    tipo_transaccion: str = None