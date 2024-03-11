from abc import ABC
from src.mercadoalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioTransacciones(Repositorio, ABC):
    ...

class RepositorioSagalog(Repositorio, ABC):
    ...