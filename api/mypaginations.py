from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 5

#     page_query_param = 'p'

#     page_size_query_param = 'records' #it will give power to client 
#     # that how many records he want on one page
#     # http://127.0.0.1:8000/api/?p=1&page=3&records=10
    
#     max_page_size = 7 #max limit of record is 7
    
#     # http://127.0.0.1:8000/api/?p=last it will show last page
#     last_page_strings = 'end' #now can put end

#  LImit Offset Pagination-------------------------
# class MyLimitOffsetPagination(LimitOffsetPagination):
    # http://127.0.0.1:8000/api/?limit=4&offset=6
    # default_limit = 5

    # limit_query_param = 'mylimit'
    # # http://127.0.0.1:8000/api/?mylimit=5&offset=6

    # offset_query_param = 'myoffset'
    # # http://127.0.0.1:8000/api/?mylimit=5&myoffset=5

    # max_limit = 3

class MyCursorPagination(CursorPagination):
    page_size = 3
    # we needed created field to manage the timestamp to solve we use ordering
    ordering = 'name'
    # it will give previous and next option

    cursor_query_param = 'cu'
