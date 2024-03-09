from abc import ABC, abstractmethod
from dataclasses import dataclass
from .comandos import ejecutar_comando, Comando
import uuid
import datetime

from ..dominio.eventos import EventoDominio
from ...modulos.mercado.aplicacion.comandos.crear_transaccion import CrearTransaccion
from ...modulos.sagas.aplicacion.comandos.propiedades import CambiarEstadoPropiedad


class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID

    @abstractmethod
    def persistir_en_saga_log(self, mensaje):
        ...

    @abstractmethod
    def construir_comando(self, evento: EventoDominio, tipo_comando: type) -> Comando:
        ...

    def publicar_comando(self, evento: EventoDominio, tipo_comando: type):
        comando = construir_comando(evento, tipo_comando)
        ejecutar_comando(comando)

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
        for i, paso in enumerate(pasos):
            if not isinstance(paso, Transaccion):
                continue

            if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                return paso, i
        raise Exception("Evento no hace parte de la transacción")

    def obtener_paso_dado_prueba(self):
        for i, paso in enumerate(pasos):
            return paso, i

    def es_ultima_transaccion(self, index):
        return len(self.pasos) - 1

    def procesar_evento(self, evento: EventoDominio):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        if self.es_ultima_transaccion(index) and not isinstance(evento, paso.error):
            self.terminar()
        elif isinstance(evento, paso.error):
            self.publicar_comando(evento, self.pasos[index - 1].compensacion)
        elif isinstance(evento, paso.evento):
            self.publicar_comando(evento, self.pasos[index + 1].compensacion)

    def procesar_evento_prueba(self):
        comando = None
        for i, paso in enumerate(self.pasos):
            if hasattr(paso, 'comando'):
                if paso.comando == CrearTransaccion:
                    comando = CrearTransaccion(fecha_creacion="", fecha_actualizacion="",id="", id_propiedad="", tipo_transaccion="")
                elif paso.comando == CambiarEstadoPropiedad:
                    comando = CambiarEstadoPropiedad()
                if comando is not None:
                    comando.health()
