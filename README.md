# propiedades-alpes-inseparables

## Instrucciones para el despliegue
1. En gitpod, crear un workspace con el código del repositorio
2. En la terminarl de gitpod, ejecutar el comando:
```gp validate```
3. En una nueva terminal en gitpod, ejecutar el comando que permite subir el perfil de pulsar:
```docker-compose --profile pulsar up --build -d```
4. Cada uno de los microservicios se pueden subir de manera independiente con los siguientes comandos:
   
```flask --app src/mercadoalpes/api run -p 5000```

```flask --app src/propiedadesalpes/api run -p 5001```

```flask --app src/clientesalpes/api run -p 5002```

uvicorn src.bff_web.main:app --host localhost --port 8003 


## Instrucciones para la ejecución
Tenga en cuenta las URL y puertos suministrados por GitPod para la ejecición de la prueba
* Ejecutar la siguiente instrucción para crear un cliente propietario con una propiedad
```curl --location '{{url_servicio_mercado_gitpod}}/cliente/cliente-asincrona' \--header 'Content-Type: application/json' \--data '"id_cliente": "1", "nombre_cliente": "Nombre cliente", "tipo_cliente": "Propietario", "propiedad": { "id_propiedad": "82b98179-6971-43d6-ada6-8c28d85e2c59", "nombre_propiedad" : "Nombre propiedad", "estado_propiedad":"LIBRE", "cliente_propiedad": "1" }'```

* Ejecutar la siguiente instrucción para crear una transaccion sobre una propiedad
```curl --location '{{url_servicio_mercado_gitpod}}/propiedades/transaccion' \--header 'Content-Type: application/json' \--data '{"id_propiedad":"a10636ff-6783-46c6-a359-60581f22a80b", "tipo_transaccion":"VENTA"}'```
* Para probar el BBF
  
  1.Query

  ![image](https://github.com/JuanSebastianBecerra/propiedades-alpes-inseparables/assets/20029761/b74ae69c-0291-48ce-b1ec-d4ad8f5a9b3f)

  2. Mutation

  ![image](https://github.com/JuanSebastianBecerra/propiedades-alpes-inseparables/assets/20029761/4e29f34a-950a-4ba8-b37d-57e9e6510a44)

## Listado de actividades
| Actividad                                          | Responsable            |
|----------------------------------------------------|------------------------|
| Creación de repositorio                            | Juan Sebastián Becerra |
| Mapas de contexto ASIS, TOBE                       | Nicolás Gómez          |
| Dominios, subdominios y contextos en ContextMapper | Mónica Bajonero        |
| Punto de vista de contexto                         | Nicolás Gómez          |
| Punto de vista funcional (módulo)                  | Nestor Pérez           |
| Punto de vista funcional (C&C)                     | Juan Sebastián Becerra |
| Punto de vista de información                      | Mónica Bajonero        |
| Atributos de modificabilidad/extensibilidad        | Mónica Bajonero        |
| Atributos de Escalabilidad                         | Nicolás Gómez          |
| Atributos de Latencia                              | Nestor Pérez           |
| Creación arquitectura hexagonal (código)           | Juan Sebastián Becerra |
| Montaje en gitpod                                  | Juan Sebastián Becerra |
| Implementación CQRS y UOW                          | Mónica Bajonero        |
| Adición módulo mercado                             | Nestor Pérez           |
| Adición módulo de propiedades                      | Mónica Bajonero        |
| Adición módulo de clientes                         | Nicolás Gómez          |
| Implementación de pulsar                           | Juan Sebastián Becerra |
| Implementación de flujo eventos y comandos         | Mónica Bajonero        |
| Implementación BFF                                 | Nestor Pérez           |
| Implementación Saga                                | Juan Sebastián Becerra |



