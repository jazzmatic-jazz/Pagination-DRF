from django.shortcuts import render
from .serializers import PersonSerializer
from .models import Person
from rest_framework.generics import ListAPIView
# from .mypaginations import MyPageNumberPagination
# from .mypaginations import  MyLimitOffsetPagination
from .mypaginations import  MyCursorPagination

class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    pagination_class = MyCursorPagination