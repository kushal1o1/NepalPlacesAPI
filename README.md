# Nepal Places API

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
- Retrieve a list of all provinces with details including:
  - **Capital City (Headquarter)**
  - **Area** (in km²)
  - **Population**
  - **Number of Districts**
  
- Fetch districts by province, including:
  - **District Headquarters**
  - **Area** (in km²)
  - **Population** (2021)
  
- Access places within each district

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

6. **Access the API at http://127.0.0.1:8000/api/provinces/**

## Documentation

For detailed API documentation, please refer to [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This project is open-source. Please see [LICENSE.md](./LICENSE.md) for details.
