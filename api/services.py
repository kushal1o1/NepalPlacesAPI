from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


from rest_framework.response import Response

class MinimalResponseMixin:
    minimal_fields = ['name']  # default minimal fields

    def list(self, request, *args, **kwargs):
        minimal = request.query_params.get('minimal', 'false').lower() == 'true'
        queryset = self.get_queryset()

        # If ?minimal=true
        if minimal:
            data = queryset.values(*self.minimal_fields)
            page = self.paginate_queryset(data)

            # ✅ Use DRF pagination dynamically
            if page is not None:
                return self.get_paginated_response(list(page))

            # ✅ If no pagination (e.g., pagination disabled)
            return Response({
                'count': len(data),
                'next': None,
                'previous': None,
                'results': list(data)
            })

        # Otherwise fallback to normal list()
        return super().list(request, *args, **kwargs)



# NOT needed for now we gonna make it sensitive its dbdata that making inconsistent
class CaseInsensitiveLookupMixin:
    """
    Mixin to make lookup_field case-insensitive.
    Use with any DRF viewset that uses a string-based lookup_field.
    """

    def get_object(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        queryset = self.filter_queryset(self.get_queryset())
        
        # Case-insensitive lookup
        filter_kwargs = {f"{self.lookup_field}__iexact": lookup_value}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # Check permissions
        self.check_object_permissions(self.request, obj)
        return obj




def error_response(code, message, details=None, http_status=status.HTTP_400_BAD_REQUEST):
    return Response({
        "success": False,
        "error": {
            "code": code,
            "message": message,
        }
    }, status=http_status)
