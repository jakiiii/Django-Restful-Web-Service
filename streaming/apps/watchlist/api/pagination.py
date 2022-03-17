from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'


class WatchListCRPagination(CursorPagination):
    page_size = 2
    ordering = '-created_at'
    cursor_query_param = 'record'
