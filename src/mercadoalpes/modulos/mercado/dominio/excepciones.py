from src.mercadoalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioPropiedadesExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de vuelos'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)