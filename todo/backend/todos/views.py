from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import TodoSerializer
from .models import TODO


class ListTodoAPI(ListAPIView):
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer


class TodoAPI(RetrieveAPIView):
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer
