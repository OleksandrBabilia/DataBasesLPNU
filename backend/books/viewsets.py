from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book, Ganre 
from .serializers import BookSerializer, GanreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]

class GanreViewSet(viewsets.ModelViewSet):
    queryset = Ganre.objects.all()
    serializer_class = GanreSerializer 
    permission_classes = [IsAuthenticated]

