from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.forms import model_to_dict

from books.models import Books
from books.serializers import BooksSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


# class BooksAPIList(generics.ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
#
#
# class BooksAPIUpdate(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
#
#
# class BooksAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer



