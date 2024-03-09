from __future__ import annotations
from dataclasses import dataclass, field

from src.mercadoalpes.seedwork.dominio.entidades import AgregacionRaiz
from src.mercadoalpes.modulos.mercado.dominio.eventos.transacciones import TransaccionCreada

import uuid

@dataclass
class Transaccion(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=None)
    tipo_transaccion: str = field(hash=True, default=None)
    

    def crear_transaccion(self, transaccion: Transaccion):
        self.id_propiedad = transaccion.id_propiedad
        self.tipo_transaccion=transaccion.tipo_transaccion
        

        self.agregar_evento(TransaccionCreada(id_propiedad=self.id_propiedad, tipo_transaccion=self.tipo_transaccion))

