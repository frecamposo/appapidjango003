from pyexpat import model
from .models import Personas,Post
from rest_framework import serializers
from django.db.models import fields

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=["id","userId","title","body"] # __all__