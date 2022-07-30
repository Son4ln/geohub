# Geo's Hub Project

## Code structure explanation

Geo's Hub online services are built using Docker, FastAPI, GRPC, Postgresql, and Nginx.

Their uses are:

- Nginx: Webserver, reverse proxy and APIs centralized.
- FastAPI: Create APIs to communicate between Geo's Hub backend and frontend.
- GRPC: Remote Procedure Calls (RPC) for internal communication between services in the system.
- Postgresql: Database for storing data.
- Docker: Containerization and management of services.

Geo's Hub is designed with 5 services including webserver(Nginx), customers, services for sale(sfs service), orders and employees.
In this source code I have built 4 services including webserver(Nginx), customers, orders, services for sale(sfs service)

The main code structure of each service is as follows:

- api_server.py: FastAPI server for the service.
- grpc_server.py: GRPC server for the service.
- models.py: Input, Output models for both APIs and RPCs.
- database: Build tables and provide methods for using data from tables.
- rest_api: REST API for the service.
- grpc_services: GRPC services(both server and clients) for the service.
- grpc_gen: GRPC generated files.

## How setup the system

- Install `docker` and `docker-compose` is required.
- Run `docker-compose build` to build the Docker images.
- Run `docker-compose up` to start the services.

### Service APIs documentation url

- customers: http://localhost:8080/api/customers/docs
- services for sale: http://localhost:8080/api/services/docs
- orders: http://localhost:8080/api/orders/docs

### Sample requests

- Create Customer:

```bash
curl --location --request POST 'localhost:8080/api/customers' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "son",
    "last_name": "dang",
    "phone": "0909445408",
    "email": "sondn0523@gmail.com",
    "address": "123 address",
}'
```

- Create Service:

```bash
curl --location --request POST 'localhost:8080/api/services' \
--header 'Content-Type: application/json' \
--data-raw '{
    "code": "ASABCD",
    "name": "ASABCD service",
    "summary": "Summary for ASABCD service",
    "description": "Desc for ASABCD service",
    "price": 45,
    "os_platform": "Windows"
}'
```

- View/Seach services:

```bash
curl --location --request GET 'localhost:8080/api/services?order_by=name&sort_asc=False&search_code=ABC&customer_id=1'
```

- View all customer activities:

```bash
curl --location --request GET 'localhost:8080/api/customers/activity'
```
