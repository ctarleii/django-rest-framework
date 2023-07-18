from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from books.models import Books
from books.permissions import IsAdminOrReadOnly
from books.serializers import BooksSerializer


class BooksApiListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 2


class BooksAPIList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = BooksApiListPagination


class BooksAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class BooksAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (IsAdminOrReadOnly, )
