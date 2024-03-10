import typing
import strawberry
import requests
import os

from datetime import datetime


MERCADO_HOST = os.getenv("MERCADO_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_transacciones(root) -> typing.List["Transaccion"]:
    transacciones_json = requests.get(f'http://{MERCADO_HOST}:5000/mercado/transaccion').json()
    transacciones = []

    for transaccion in transacciones_json:
        transacciones.append(
             Transaccion(
                id=transaccion.get('id'), 
                id_propiedad=transaccion.get('id_propiedad'),
                fecha_creacion=transaccion.get('fecha_creacion'),
                fecha_actualizacion=transaccion.get('fecha_actualizacion')
                #fecha_creacion=datetime.strptime(transaccion.get('fecha_creacion'), FORMATO_FECHA), 
                #fecha_actualizacion=datetime.strptime(transaccion.get('fecha_actualizacion'), FORMATO_FECHA),
                
            )
        )

    return transacciones



@strawberry.type
class Transaccion:
    id: str
    id_propiedad: str
    fecha_creacion: str
    fecha_actualizacion: str

@strawberry.type
class TransaccionRespuesta:
    mensaje: str
    codigo: int

@strawberry.type
class Propiedad:
    id_propiedad: str
    nombre_propiedad: str
    estado_propiedad: str
    cliente_propiedad: str



@strawberry.type
class PropiedadRespuesta:
    mensaje: str
    codigo: int




