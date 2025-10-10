# API Documentation (Currently v1)

<div align="center">

  <p>
    <a href="#api-endpoints">API Endpoints</a> · 
    <a href="#filtering-functionality">Filtering Functionality</a> · 
    <a href="#search-functionality">Search Functionality</a> · 
    <a href="#sorting-functionality">Sorting Functionality</a> · 
    <a href="#pagination">Pagination</a> · 
    <a href="#caching">Caching</a> · 
    <a href="#rate-limiting">Rate Limiting</a>
  </p>
</div>


---

## API Endpoints

## Base URL

All endpoints are versioned to allow backward compatibility and smooth upgrades.

**Format:**
```cmd
/api/{version}/{resource}/
```

**Current Version:** `v1`


### 🧩 Minimal Mode

For a lightweight response, use the query parameter `?minimal=true` in any endpoint.  
This will return **only the name field** for quick lookups or dropdowns.

- `GET /provinces?minimal=true` – List all provinces (name only)
- `GET /districts?minimal=true` – List all districts (name only)
- `GET /cities?minimal=true` – List all cities (name only)
- `GET /wards?minimal=true` – List all wards (name only)
- `GET /places?minimal=true` – List all places (name only)



### Provinces
- `GET /provinces/` - List all provinces
- `GET /provinces/{province_name}/` - Retrieve a specific province

### Districts
- `GET /districts/` - List all districts 
- `GET /provinces/{province_name}/districts/` - List all districts within a province
- `GET /provinces/{province_name}/districts/{district_name}/` - Retrieve a specific district within a province

### Cities
- `GET /cities/` - List all cities 
- `GET /provinces/{province_name}/districts/{district_name}/cities/` - List all cities within a district
- `GET /provinces/{province_name}/districts/{district_name}/cities/{city_name}/` - Retrieve a specific city within a district

### Wards
- `GET /wards/` - List all wards 
- `GET /provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/` - List all wards within a city
- `GET /provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/` - Retrieve a specific ward within a city

### Places
- `GET /places/` - List all places
- `GET /provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/places/` - List all places within a ward
- `GET /provinces/{province_name}/districts/{district_name}/cities/{city_name}/wards/{ward_name}/places/{place_name}/` - Retrieve a specific place within a ward

---

## Filtering Functionality

### Overview
The API provides filtering capabilities to refine search results based on various fields across provinces, districts, cities, wards, and places. Users can apply multiple filters to retrieve specific data using query parameters.

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

### Example: Filtering Places

#### Endpoint
`GET /places/`

#### Example Request
`GET /places/?placetype=Famous_places&name=Temple`

#### Example Response
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

### Place Types
Available options for `placetype`:
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

#### Example: Filter by Place Type
`GET /places/?placetype=Famous_places`

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

#### Example: Filter by Name
`GET /places/?name=Kalimati`

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

---

## Search Functionality

### Overview
The API provides the ability to search through different entities like provinces, districts, cities, wards, and places. This search functionality allows users to quickly locate the information they need using keyword-based search.

### Searchable Fields

- **Provinces**: `name`, `headquarters`, `districts__name`, `districts__cities__name`, `districts__cities__wards__name`, `districts__cities__wards__places__name`
- **Districts**: `name`, `headquarter`, `province`, `area`
- **Cities**: `name`, `wards__ward_no`, `wards__name`, `city_type`
- **Wards**: `ward_no`, `name`, `places__name`, `places__place_type`
- **Places**: `name`, `description`, `placetype`

### Example: Search Places

#### Endpoint
`GET /places/?search={query}`

#### Example Request
`GET /places/?search=Pashupatinath`

#### Example Response
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

---

## Sorting Functionality

### Overview
The API supports sorting for all the fields in the respective models. You can sort data in ascending or descending order using the `ordering` query parameter. By default, sorting is done in ascending order, but you can prepend a hyphen (`-`) to the field name to sort in descending order.

### Sortable Fields:
- **Provinces**: `name`, `headquarters`, `districts__name`, `districts__cities__name`, `districts__cities__wards__name`, `districts__cities__wards__places__name`
- **Districts**: `name`, `headquarter`, `province`, `area`
- **Cities**: `name`, `wards__ward_no`, `wards__name`, `city_type`
- **Wards**: `ward_no`, `name`, `places__name`, `places__place_type`
- **Places**: `name`, `description`, `placetype`

### Example: Sorting Places

#### Endpoint
`GET /places/?ordering={field}`

#### Example Requests
1. Sort places by name in ascending order:
   `GET /places/?ordering=name`

2. Sort places by population in descending order:
   `GET /places/?ordering=-population`

---

## Pagination

### Overview
The API supports pagination to manage large datasets efficiently. Pagination breaks down the results into pages, making it easier to navigate through large collections of provinces, districts, cities, wards, or places.

### Pagination Parameters

- **page**: Specifies the page number of the results you want to retrieve. Default is the first page.
- **page_size**: Specifies the number of records per page. You can control how many results appear in each page by passing this parameter.

### Example: Paginated Request for Places

#### Endpoint
`GET /places/`

#### Example Request
`GET /places/?page=2&page_size=5`

#### Example Response
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
    ]
}
```

---

## Caching

### Overview
Caching is implemented to improve performance and reduce response times for frequent API requests. Caching helps minimize database queries by storing the results of expensive operations.

### Implementation
We have implemented caching using **Redis**. This allows us to store frequently accessed data in memory, reducing the load on the database and speeding up response times for high-traffic endpoints.

### Benefits of Caching

- **Improved Performance**: Reduces database hits and speeds up API response times.
- **Scalability**: Handles high traffic efficiently by caching frequently accessed data.
- **Resource Optimization**: Frees up database resources for other operations.

### Prerequisites
- Ensure you have **Django** and **Django REST Framework** installed.
- Install **Redis** on your server or use a cloud-based Redis service.

---

## Rate Limiting

### Overview
Rate limiting is a technique used to control the amount of incoming requests to an API, helping to prevent abuse and ensuring fair usage among users. This feature limits the number of requests a user can make to the API within a specified time frame.

### Why Use Rate Limiting?

- **Prevent Abuse:** Protects the API from being overwhelmed by too many requests from a single user.
- **Fair Usage:** Ensures that all users have equal access to the API resources.
- **Cost Management:** Helps in managing the costs associated with server resources and bandwidth usage.
- **Enhanced Security:** Reduces the risk of denial-of-service attacks.

### Implementation

We have implemented rate limiting using the `django_ratelimit` library. The `@ratelimit` decorator is used in viewsets to specify the rate limit.

#### Example:
In the `ProvinceViewSet`, we set a limit of **5 requests per minute** per IP address:

```python
@method_decorator(ratelimit(key='ip', rate='5/m', method='GET', block=False))
```