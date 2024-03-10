from src.bff_web.comandosIntegracion import ComandoIntegracion
import strawberry
import typing
import uuid

from strawberry.types import Info
from src.bff_web import utils
from src.bff_web.despachadores import Despachador

from .esquemas import *


@strawberry.type
class Mutation:


    @strawberry.mutation
    async def registrar_propiedad(self, id_propiedad: str, nombre_propiedad: str, estado_propiedad: str, cliente_propiedad: str, info: Info) -> PropiedadRespuesta:
        print(f"ID Propiedad: {id_propiedad}, Tipo Transaccion: {nombre_propiedad}")
        propiedad = Propiedad(
            id_propiedad = id_propiedad,
            nombre_propiedad = nombre_propiedad,
            estado_propiedad = estado_propiedad,
            cliente_propiedad = cliente_propiedad
        )
  
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_comando, propiedad, "comandos-cliente")
        
        return PropiedadRespuesta(mensaje="Procesando Mensaje", codigo=203)



       