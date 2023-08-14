from rest_framework import serializers
from . models import Category, Portfolio , Services


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__alls__"

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'



