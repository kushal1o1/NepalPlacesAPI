# Project Coding Standards

## 1. Variable Naming
- Use snake_case for variables/functions: `user_profile`, `get_user_data()`
- Use PascalCase for class names: `UserProfile`

## 2. Model Rules
- Use `Meta: verbose_name` for admin display
- `__str__` should return human-readable string

## 3. Views
- Use class-based views (CBV) where possible
- Logic-heavy views → move logic to `services/`

## 4. Logging
- Avoid print()
- Use `logger.info()` and `logger.error()` with proper messages

## 5. Folder Structure
- `common/` for shared logic
- `services/` for business logic
- `serializers/`, `forms/`, `validators/` etc. must be modular

## 6. Error Handling
- Always catch exceptions at service level, not views
- Log the error and return user-friendly messages

## 7. Testing
- Write tests for every model/view/form
- Use `pytest` + `pytest-django`

## 8. Environment Files
- Keep `.env.example` committed 
-  `.env`

## 9. Admin default Password
-user id `admin1`
-password `openadmin`

## 10. Maintain API versioning
```cmd
/api/{version}/{resource}/
```

## 11. Maintain RESTFUL API standards
