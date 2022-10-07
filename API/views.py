from .models import Post,Personas
from .serializers import PostSerializers
from rest_framework import generics

# Create your views here.
class PostViewSet(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostSearchSet(generics.ListAPIView):
    serializer_class = PostSerializers
    def get_queryset(self):
        id_post = self.kwargs['id']
        return Post.objects.filter(id=id_post)