from LibraryApp.models import Library
from LibraryApp.api.serializers import LibrarySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from LibraryApp.models import Library
from rest_framework.permissions import IsAuthenticated




class LibraryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Library.objects.all()
        serializer = LibrarySerializer(books,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class LibraryDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,pk):
        try:
            book = Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            return Response({'error':'Book not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = LibrarySerializer(book)
        return Response(serializer.data)

    def put(self, request,pk):
        book = Library.objects.get(pk=pk)
        serializer = LibrarySerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        book = Library.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
