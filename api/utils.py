from rest_framework.views import exception_handler
from django.http import JsonResponse
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {
            "success": False,
            "error": {
                "code": exc.__class__.__name__,
                "message": str(exc.detail) if hasattr(exc, 'detail') else str(exc)
            }
        }
    return response


def custom_404_handler(request, exception=None):
    return JsonResponse({
        "success": False,
        "error": {
            "code": "NotFound",
            "message": '''The requested endpoint does not exist. Please refer to the API documentation for valid endpoints.'''
        }
    }, status=status.HTTP_404_NOT_FOUND)
    
    
def custom_500_handler(request):
    return JsonResponse({
        "success": False,
        "error": {
            "code": "InternalServerError",
            "message": "An unexpected error occurred on the server."
        }
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
