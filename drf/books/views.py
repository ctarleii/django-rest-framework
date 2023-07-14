from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from books.models import Books
from books.serializers import BooksSerializer


class BooksApiView(APIView):
    def get(self, request):
        w = Books.objects.all()
        return Response({'posts': BooksSerializer(w, many=True).data})

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Books.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']

        )
        return Response({'post': BooksSerializer(post_new).data})

# class BooksApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
