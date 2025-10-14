<div align="center">
  <h1>Nepal Places API</h1>
</div>

<div align="center">
  <p>
    <a href="./API_DOCUMENTATION.md">API Documentation</a> · 
    <a href="./CONTRIBUTING.md">Contributing Guidelines</a> · 
    <a href="./LICENSE.md">License</a>
  </p>
</div>


## Overview
Nepal Places API is an open-source RESTful API that provides detailed information about the geographical divisions of Nepal. It allows users to access data about provinces, districts, and places, including headquarters, area, population, and the number of districts in each province.

## Features
- Retrieve detailed province data — including capital, area (km²), population, and district count.
- Fetch districts by province — with headquarters, area, and 2021 population details.
- Access places within each district for deeper geographic insights.
- Support for minimal data retrieval to optimize performance.
- Versioned API to ensure backward compatibility.
- Comprehensive error handling and validation.
- Search and filter capabilities for efficient data access.
- Caching and rate limiting to enhance performance and security.

## Installation

### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Steps to Install

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kushal1o1/NepalPlacesAPI.git
   cd NepalPlacesAPI
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```


3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Django server:**
   ```bash
   python manage.py runserver
   ```

**Using Docker:**
   ```bash
   docker-compose up --build
   ```

6. **Access the API at http://127.0.0.1:8000/api/v1/**

## Documentation

| **Section**      | **Feature**          | **Description / Example**                                                                              |
| ---------------- | -------------------- | ------------------------------------------------------------------------------------------------------ |
| **Base URL**     | Format               | `/api/{version}/{resource}/`                                                                           |
|                  | Current Version      | `v1`                                                                                                   |
|                  | **Success Response** | ```json{ "count": 7, "next": null, "previous": null, "results": [] }```                                        |
|                  | **Failure Response** | `{ "success": false, "error": {"code": "VALIDATION_ERROR", "message": "District name is required."} }` |
| **Minimal Mode** | Query                | `?minimal=true` → returns only the `name` field                                                        |
|                  | Example              | `/provinces?minimal=true`, `/places?minimal=true`                                                      |
| **Endpoints**    | Provinces            | `/provinces/`, `/provinces/{province_name}/`                                                           |
|                  | Districts            | `/districts/`, `/provinces/{province_name}/districts/{district_name}/`                                 |
|                  | Cities               | `/cities/`, `/provinces/{p}/districts/{d}/cities/{c}/`                                                 |
|                  | Wards                | `/wards/`, `/provinces/{p}/districts/{d}/cities/{c}/wards/{w}/`                                        |
|                  | Places               | `/places/`, `/provinces/{p}/districts/{d}/cities/{c}/wards/{w}/places/{place}/`                        |


For detailed API documentation, please refer to [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This project is open-source. Please see [LICENSE.md](./LICENSE.md) for details.
