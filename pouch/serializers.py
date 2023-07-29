
from django.db.models import fields
from rest_framework import serializers
from .models import Pouch
 
class PouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pouch
        fields = '__all__'