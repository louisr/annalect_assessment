# U.S. Crude Oil Imports Service

A API service for data on U.S. Crude Oil Imports.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Start the containers:

   ```bash
   docker-compose up -d --build
   ```

2. Create database and run migrations:
   ```bash
   docker-compose exec api app/scripts/create_database.py
   docker-compose exec api alembic upgrade head
   ```

3. Execute load data script:
   ```bash
   docker-compose exec api python scripts/load_data.py
   ```

4. Browse http://localhost:8000/docs


## Requirements
- Python
- Postgresql


## API Endpoints


### /imports/

#### POST
##### Summary:

Create Import

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

#### GET
##### Summary:

Get Imports

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| skip | query |  | No | integer |
| limit | query |  | No | integer |
| countryName | query |  | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### /imports/{import_id}

#### GET
##### Summary:

Get Import

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| import_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### PATCH
##### Summary:

Update Import

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| import_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### DELETE
##### Summary:

Delete Import

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| import_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | Successful Response |
| 422 | Validation Error |

Visit http://localhost:8000/docs for indepth representation of the API.
