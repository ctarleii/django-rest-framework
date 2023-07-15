from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from books.models import Books
from books.serializers import BooksSerializer


class BooksAPIList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksApiView(APIView):
    def get(self, request):
        w = Books.objects.all()
        return Response({'posts': BooksSerializer(w, many=True).data})

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        print(f'put {kwargs}')
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Books.objects.get(pk=pk)
        except:
            return Response({'error': "Object doesn't not exists"})

        serializer = BooksSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            Books.objects.get(id=pk).delete()
        except:
            return Response({'error': "Object doesn't not exists"})

        return Response({'post': f'delete post {pk}'})
