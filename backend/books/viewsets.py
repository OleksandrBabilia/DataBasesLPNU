from rest_framework import viewsets
from .models import Book, Ganre 
from .serializers import BookSerializer, GanreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 


class GanreViewSet(viewsets.ModelViewSet):
    queryset = Ganre.objects.all()
    serializer_class = GanreSerializer 

