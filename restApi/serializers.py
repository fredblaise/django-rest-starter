# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Portfolio, Project


# create a model serializer
class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    # specify models and fields
    class Meta:
        model = Portfolio
        fields = (
            "id",
            "title",
            "subtitle",
            "hero_image",
            "mini_about",
            "about",
        )


# create a model serializer
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # specify models and fields
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "link",
            "img_url",
            "rank",
            "is_featured",
        )
