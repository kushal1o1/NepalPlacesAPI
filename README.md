# Nepal Places API

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
  
- Access places within each district.

## API Endpoints
### Provinces
- `GET /api/provinces/` - List all provinces
- `GET /api/provinces/{province_name}/` - Retrieve a specific province

### Districts
- `GET /api/provinces/{province_name}/districts/` - List all districts within a province
- `GET /api/provinces/{province_name}/districts/{district_name}/` - Retrieve a specific district within a province

### Cities
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/` - List all cities within a district
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/` - Retrieve a specific city within a district

### Wards
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/` - List all wards within a city
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/` - Retrieve a specific ward within a city

### Places
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/places/` - List all places within a ward
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/places/{place_name}/` - Retrieve a specific place within a ward
## Installation

### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Steps to Install

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/nepal-places-api.git
   cd nepal-places-api
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
6.**Access the API at http://127.0.0.1:8000/api/provinces/.**

## Contributing

We welcome contributions to the Nepal Places API project! To contribute, please follow these steps:

1. **Fork the repository.**
   - Click the "Fork" button at the top right of the repository page on GitHub to create your copy of the repository.

2. **Clone the repository to your local machine:**
   ```bash
   git clone https://github.com/yourusername/nepal-places-api.git
   cd nepal-places-api
3. **Create a new branch for your feature or bug fix:**
   ```bash
   git checkout -b feature-branch
   ```
4. **Make your changes.**
   - Add new features or fix bugs in the codebase.

5. **Commit your changes:**
   ```bash
   git commit -m "Add a descriptive message about your changes"
   ```
6. **Push to your forked repository:**
   ```bash
   git push origin feature-branch
    ```
7. **Open a Pull Request (PR).**
   - Go to the original repository on GitHub.
   - Click on the "Pull Requests" tab.
   - Click the "New Pull Request" button.
   - Select your branch and submit the PR with a description of your changes.

### Guidelines
- **Code Style**: Follow the existing code style in the project.
- **Documentation**: If you add new features, consider updating the documentation.
- **Tests**: Include tests for new features and ensure existing tests pass.

### Issues
If you encounter any issues or have questions about contributing, please feel free to open an issue in the repository.

Thank you for your contributions!
