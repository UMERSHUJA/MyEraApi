from rest_framework import serializers
from startup.models import Startup

class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ['id', 'product_name', 'description', 'image','prices', 'facebook', 'twitter', 'is_sponsered']
