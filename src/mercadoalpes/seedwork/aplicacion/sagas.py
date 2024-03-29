from abc import ABC, abstractmethod
from dataclasses import dataclass
from .comandos import ejecutar_comando, Comando
import uuid
import datetime

from ..dominio.eventos import EventoDominio


class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID

    @abstractmethod
    def persistir_en_saga_log(self, mensaje):
        ...

    @abstractmethod
    def construir_comando(self, evento: EventoDominio, tipo_comando: type, index_paso: int) -> Comando:
        ...

    def publicar_comando(self,mensaje, evento: EventoDominio, tipo_comando: type, index_paso: int):
        comando = self.construir_comando(mensaje, evento, tipo_comando, index_paso)
        # ejecutar_comando(comando)


    @abstractmethod
    def inicializar_pasos(self):
        ...

    @abstractmethod
    def procesar_evento(self, evento: EventoDominio):
        ...

    @abstractmethod
    def iniciar(self):
        ...

    @abstractmethod
    def terminar(self):
        ...


class Paso():
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime
    index: int


@dataclass
class Inicio(Paso):
    index: int = 0


@dataclass
class Fin(Paso):
    ...


@dataclass
class Transaccion(Paso):
    index: int
    comando: Comando
    evento: EventoDominio
    error: EventoDominio
    compensacion: Comando


class CoordinadorOrquestacion(CoordinadorSaga, ABC):

    def __init__(self):
        self.pasos = None
        self.index: int = 0

    def set_pasos(self, pasos):
        self.pasos: list[Paso] = pasos

    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        for i, paso in enumerate(self.pasos):
            if not isinstance(paso, Paso):
                continue
               
            if hasattr(paso, 'evento') or hasattr(paso, 'error'):
                # if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                if type(evento) == type(paso.evento) or type(evento) == type(paso.error):
                    return paso, i
        raise Exception("Evento no hace parte de la transacción")


    def es_ultima_transaccion(self, index):
        return len(self.pasos) - 1 == index

    def procesar_evento(self, mensaje, evento: EventoDominio):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        if self.es_ultima_transaccion(index) and not type(evento) == type(paso.error):
            self.terminar()
        elif type(evento) == type(paso.error):
            self.publicar_comando(mensaje, evento, self.pasos[index - 1].compensacion, index)
        elif isinstance(evento, paso.evento) or type(evento) == type(paso.evento):
            self.publicar_comando(mensaje, evento, self.pasos[index + 1].comando, index)
