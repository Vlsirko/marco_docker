from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ProductListPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):

        return Response({
            'per_page': self.page.paginator.per_page,
            'num_pages': self.page.paginator.num_pages,
            'current': self.page.number,
            'count': self.page.paginator.count,
            'results': data
        })