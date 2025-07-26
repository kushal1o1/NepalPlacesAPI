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



## Overview

This API allows you to retrieve a list of places, with filtering capabilities based on several parameters. You can filter places by `placetype` and `name`. The filtering options are case-sensitive and help refine your search to find relevant places.
## API Endpoints
### Provinces
- `GET /api/provinces/` - List all provinces
- `GET /api/provinces/{province_name}/` - Retrieve a specific province

### Districts
- `GET /api/districts/` - List all districts 
- `GET /api/provinces/{province_name}/districts/` - List all districts within a province
- `GET /api/provinces/{province_name}/districts/{district_name}/` - Retrieve a specific district within a province

### Cities
- `GET /api/cities/` - List all cities 
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/` - List all cities within a district
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/` - Retrieve a specific city within a district

### Wards
- `GET /api/wards/` - List all wards 
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/` - List all wards within a city
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/` - Retrieve a specific ward within a city

### Places
- `GET /api/places/` - List all places
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/places/` - List all places within a ward
- `GET /api/provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/places/{place_name}/` - Retrieve a specific place within a ward

## API Documentation
# Nepal Places API - Filtering Functionality

## Overview
The API provides filtering capabilities to refine search results based on various fields across provinces, districts, cities, wards, and places. Users can apply multiple filters to retrieve specific data using query parameters.

## Filtering Fields

### 1. Provinces
You can filter provinces by the following fields:
- **name**: Partial match (case-insensitive)
- **headquarters**: Partial match (case-insensitive)
- **min_area**: Minimum area (km²)
- **max_area**: Maximum area (km²)
- **min_population**: Minimum population
- **max_population**: Maximum population
- **min_districts**: Minimum number of districts
- **max_districts**: Maximum number of districts
- **district_name**: Partial match for district names (case-insensitive)
- **district_headquarters**: Partial match for district headquarters (case-insensitive)
- **min_district_area**: Minimum district area (km²)
- **max_district_area**: Maximum district area (km²)
- **min_district_population**: Minimum district population
- **max_district_population**: Maximum district population
- **city_name**: Partial match for city names (case-insensitive)
- **place_name**: Partial match for place names (case-insensitive)

### 2. Districts
You can filter districts by the following fields:
- **min_area**: Minimum area (km²)
- **max_area**: Maximum area (km²)
- **min_population**: Minimum population
- **max_population**: Maximum population
- **province_name**: Exact match for province name

### 3. Cities
You can filter cities by the following fields:
- **district_name**: Exact match for district name
- **city_type**: Filter by city type (e.g., metropolitan, municipality)

### 4. Wards
You can filter wards by the following fields:
- **city_name**: Exact match for city name
- **ward_no**: Filter by specific ward number

### 5. Places
You can filter places by the following fields:
- **placetype**: Exact match (case-insensitive)
- **name**: Partial match (case-insensitive)

## Example: Filtering Places

### Endpoint
- **GET /api/places/**

### Example Request
- **GET /api/places/?placetype=Famous_places&name=Temple**

### Example Response
```json
[
    {
        "name": "Pashupatinath Temple",
        "ward": "Ward No. 7",
        "description": "One of the most sacred Hindu temples.",
        "placetype": "Religious_places"
    }
]
```

## Query Parameters for Filtering
## GET /api/places/
### 1. `placetype`

Filters places by the type of place. The available options for `placetype` are:

- `Famous_places`: Famous Places
- `Religious_places`: Religious Places
- `Historical_sites`: Historical Sites
- `Natural_attractions`: Natural Attractions
- `Cultural_sites`: Cultural Sites
- `Educational_institions`: Educational Institutions
- `Healthcare_facilities`: Healthcare Facilities
- `Commercial_areas`: Commercial Areas
- `Residential_areas`: Residential Areas
- `Public_services`: Public Services

## GET /api/places/?placetype=Famous_places 
#### Example Response:
```json
[
    {
        "name": "Pashupatinath Temple",
        "description": "One of the most sacred Hindu temples.",
        "placetype": "Religious_places"
    },
    {
        "name": "Bouddhanath Stupa",
        "description": "One of the largest stupas in Nepal.",
        "placetype": "Religious_places"
    }
] 
```
### 2. `name`
Filters places by the  name. The name should be the exact name of the ward as listed.

## GET /api/places/?name=Kalimati
#### Example Response:
```json
[
   {
      "name": "Kalimati",
      "description": "A popular residential area in Pokhara.",
      "placetype": "Residential_areas"
      }
      ]
```
### 3. Combined Filtering
## Query Parameters for Combined Filtering

You can combine the following parameters:

- **`placetype`**: Type of place (e.g., `Famous_places`, `Religious_places`, `Historical_sites`, etc.)
- **`name`**: The exact name of the place.

## Example Combined Filter Request

To filter places based on both place type and ward name, you can use:

## Overview

This API allows combining multiple filters to refine your search. You can filter places by both `placetype` and `ward_name` at the same time.





# Nepal Places API - Search Functionality

## Overview
The API provides the ability to search through different entities like provinces, districts, cities, wards, and places. This search functionality allows users to quickly locate the information they need using keyword-based search.

## Searchable Fields

- **Provinces**: `name`, `headquarters`, `districts__name`, `districts__cities__name`, `districts__cities__wards__name`, `districts__cities__wards__places__name`
- **Districts**: `name`, `headquarter`, `province`,`area`
- **Cities**: `name`, `wards__ward_no`,`wards__name`, `city_type`
- **Wards**: `ward_no`,`name`,`places__name`,`places__place_type`
- **Places**: `name`, `description`, `placetype`

## Example: Search Places

### Endpoint
- **GET /api/places/?search={query}**

### Example Request
- **GET /api/places/?search=Pashupatinath**

### Example Response
```json
[
    {
        "name": "Pashupatinath Temple",
        "ward": "Ward No. 7",
        "description": "One of the most sacred Hindu temples.",
        "placetype": "Religious_places"
    }
]
```
# Nepal Places API - Sorting Functionality

## Overview
The API supports sorting for all the fields in the respective models. You can sort data in ascending or descending order using the `ordering` query parameter. By default, sorting is done in ascending order, but you can prepend a hyphen (`-`) to the field name to sort in descending order.

## Sorting Fields
All fields across provinces, districts, cities, wards, and places are sortable.

### Sortable Fields:
- **Provinces**: `name`, `headquarters`, `districts__name`, `districts__cities__name`, `districts__cities__wards__name`, `districts__cities__wards__places__name`
- **Districts**: `name`, `headquarter`, `province`,`area`
- **Cities**: `name`, `wards__ward_no`,`wards__name`, `city_type`
- **Wards**: `ward_no`,`name`,`places__name`,`places__place_type`
- **Places**: `name`, `description`, `placetype`

## Example: Sorting Places

### Endpoint
- **GET /api/places/?ordering={field}**

### Example Requests
1. Sort places by name in ascending order:
   - **GET /api/places/?ordering=name**

2. Sort places by population in descending order:
   - **GET /api/places/?ordering=-population**

## Summary
You can use the `ordering` parameter to sort records by any of the sortable fields listed above. For descending order, prepend a hyphen (`-`) to the field name.


# Nepal Places API - Pagination Functionality

## Overview
The API supports pagination to manage large datasets efficiently. Pagination breaks down the results into pages, making it easier to navigate through large collections of provinces, districts, cities, wards, or places. The pagination is controlled using the `page` and `page_size` query parameters.

## Pagination Parameters

### 1. `page`
Specifies the page number of the results you want to retrieve. Default is the first page.

### 2. `page_size`
Specifies the number of records per page. You can control how many results appear in each page by passing this parameter. If not provided, the default page size will be used.

## Example: Paginated Request for Places

### Endpoint
- **GET /api/places/**

### Example Request
- **GET /api/places/?page=2&page_size=5**

### Example Response
```json
{
    "count": 50,
    "next": "http://127.0.0.1:8000/api/places/?page=3&page_size=5",
    "previous": "http://127.0.0.1:8000/api/places/?page=1&page_size=5",
    "results": [
        {
            "name": "Bouddhanath Stupa",
            "ward": "Ward No. 6",
            "description": "One of the largest stupas in Nepal.",
            "placetype": "Religious_places"
        },
        {
            "name": "Pokhara Lakeside",
            "ward": "Ward No. 1",
            "description": "Famous tourist attraction in Pokhara.",
            "placetype": "Natural_attractions"
        }
        // Additional results
    ]
}
```

# Caching Feature for Province API

## Overview

This section describes the implementation of caching in the Province API to improve performance and reduce response times for frequent API requests. Caching helps minimize database queries by storing the results of expensive operations, allowing subsequent requests for the same data to be served from cache instead of hitting the database.


To enhance the performance of the API, we have implemented caching using **Redis**. This allows us to store frequently accessed data in memory, reducing the load on the database and speeding up response times for high-traffic endpoints.

##

## Benefits of Caching

- **Improved Performance**: Reduces database hits and speeds up API response times.
- **Scalability**: Handles high traffic efficiently by caching frequently accessed data.
- **Resource Optimization**: Frees up database resources for other operations.

## Setup Instructions

### Prerequisites

- Ensure you have **Django** and **Django REST Framework** installed.
- Install **Redis** on your server or use a cloud-based Redis service.


## Rate Limiting

### Overview

Rate limiting is a technique used to control the amount of incoming requests to an API, helping to prevent abuse and ensuring fair usage among users. This feature limits the number of requests a user can make to the API within a specified time frame.

### Why Use Rate Limiting?

- **Prevent Abuse:** Protects the API from being overwhelmed by too many requests from a single user, which could lead to performance degradation or downtime.
- **Fair Usage:** Ensures that all users have equal access to the API resources, preventing any single user from monopolizing the service.
- **Cost Management:** Helps in managing the costs associated with server resources and bandwidth usage, especially in cloud environments where pricing may depend on usage.
- **Enhanced Security:** Reduces the risk of denial-of-service attacks by limiting the number of requests an attacker can make.

### Implementation

In this project, we have implemented rate limiting using the `django_ratelimit` library. Below are the key components of the implementation:

**Decorator Usage:**

   The `@ratelimit` decorator is used in the viewset to specify the rate limit. For example, in the `ProvinceViewSet`, we set a limit of **5 requests per minute** per IP address.

   ```python
   @method_decorator(ratelimit(key='ip', rate='5/m', method='GET', block=False)) #5 request per min 
```
## Installation

### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Steps to Install

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kushal1o1/nepal-places-api.git
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
6. **Access the API at http://127.0.0.1:8000/api/provinces/.**

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
