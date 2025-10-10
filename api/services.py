from rest_framework.response import Response


class MinimalResponseMixin:
    minimal_fields = ['name']  # default fields

    def list(self, request, *args, **kwargs):
        minimal = request.query_params.get('minimal', 'false').lower() == 'true'
        queryset = self.get_queryset()

        if minimal:
            data = queryset.values(*self.minimal_fields)
            return Response(data)

        return super().list(request, *args, **kwargs)
