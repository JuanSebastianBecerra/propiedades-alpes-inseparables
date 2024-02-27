from src.propiedadesalpes.seedwork.aplicacion.queries import QueryHandler
from src.propiedadesalpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from src.propiedadesalpes.modulos.propiedades.dominio.fabricas import _FabricaTransaccion

class TransaccionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transacciones: _FabricaTransaccion = _FabricaTransaccion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_transacciones(self):
        return self._fabrica_transacciones    