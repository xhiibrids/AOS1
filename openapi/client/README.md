# swagger-client
Asignatura AOS: grupo 8

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [aos](aos)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientesApi(swagger_client.ApiClient(configuration))
id_cliente = 56 # int | **ID**.   ID del cliente.  type: number format: uuid

try:
    # Devuelve todas las facturas de un cliente.
    api_response = api_instance.api_facturas_get(id_cliente)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientesApi->api_facturas_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *{schema}://{server}:{port}/{basePath}*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClientesApi* | [**api_facturas_get**](docs/ClientesApi.md#api_facturas_get) | **GET** /clientes/{idCliente}/facturas/ | Devuelve todas las facturas de un cliente.
*FacturasApi* | [**api_facturas_cget**](docs/FacturasApi.md#api_facturas_cget) | **GET** /facturas | Devuelve todas las facturas existentes
*FacturasApi* | [**api_facturas_coptions**](docs/FacturasApi.md#api_facturas_coptions) | **OPTIONS** /facturas | Provides the list of HTTP supported methods.
*FacturasApi* | [**api_facturas_delete**](docs/FacturasApi.md#api_facturas_delete) | **DELETE** /facturas/{id} | Elimina el recurso Factura.
*FacturasApi* | [**api_facturas_get**](docs/FacturasApi.md#api_facturas_get) | **GET** /facturas/{id} | Devuelve una factura tras especificar su ID.
*FacturasApi* | [**api_facturas_options_id**](docs/FacturasApi.md#api_facturas_options_id) | **OPTIONS** /facturas/{id} | Provides the list of HTTP supported methods.
*FacturasApi* | [**api_facturas_post**](docs/FacturasApi.md#api_facturas_post) | **POST** /facturas | Crea una factura.
*FacturasApi* | [**api_facturas_put**](docs/FacturasApi.md#api_facturas_put) | **PUT** /facturas/{id} | Actualiza una factura determinada especificando su identificador y los campos a actualizar

## Documentation For Models

 - [Factura](docs/Factura.md)
 - [FacturaRequestBody](docs/FacturaRequestBody.md)
 - [HTTPProblem](docs/HTTPProblem.md)
 - [Trabajo](docs/Trabajo.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

aosgrupo8@aos.com