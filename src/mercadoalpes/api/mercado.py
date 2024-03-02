import src.mercadoalpes.seedwork.presentacion.api as api
import json
from src.mercadoalpes.modulos.mercado.aplicacion.servicios import ServicioTransaccion
from src.mercadoalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request, jsonify
from flask import Response
from src.mercadoalpes.modulos.mercado.aplicacion.mapeadores import MapeadorTransaccionDTOJson
from src.mercadoalpes.modulos.mercado.aplicacion.comandos.crear_transaccion import CrearTransaccion
from src.mercadoalpes.modulos.mercado.aplicacion.queries.obtener_transaccion import ObtenerTransaccion
from src.mercadoalpes.seedwork.aplicacion.comandos import ejecutar_comando
from src.mercadoalpes.seedwork.aplicacion.queries import ejecutar_query


bp = api.crear_blueprint('mercado', '/mercado')


@bp.route('/transaccion', methods=('POST',))
def registrar_transaccion():
    try:
        transaction_dict = request.json
        
        map_transaction = MapeadorTransaccionDTOJson()
        transaction_dto = map_transaction.externo_a_dto(transaction_dict)
        st = ServicioTransaccion()
        dto_final = st.crear_transaccion(transaction_dto)
        return map_transaction.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route("/transaccion-asincrona", methods=('POST',))
def registrar_transaccion_asincrona():
    try:

        transaction_dict = request.json

        map_transaction = MapeadorTransaccionDTOJson()
        transaction_dto = map_transaction.externo_a_dto(transaction_dict)

        comando = CrearTransaccion(transaction_dto.fecha_creacion, transaction_dto.fecha_actualizacion, transaction_dto.id, transaction_dto.id_propiedad)
        ejecutar_comando(comando)
        return Response({}, status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/transaccion', methods=('GET',))
@bp.route('/transaccion/<id>', methods=('GET',))
def dar_transaccion(id=None):
    st = ServicioTransaccion()
    if id:
        return st.obtener_transaccion_por_id(id)
    else:
        return jsonify(st.obtener_todos())


@bp.route('/transaccion-query', methods=('GET',))
@bp.route('/transaccion-query/<id>', methods=('GET',))
def dar_transaccion_query(id=None):
    st = ServicioTransaccion()
    if id:
        query_resultado = ejecutar_query(ObtenerTransaccion(id))
        map_transaccion = MapeadorTransaccionDTOJson()

        return map_transaccion.dto_a_externo(query_resultado.resultado)
    else:
        return [{"message": "GET"}]

