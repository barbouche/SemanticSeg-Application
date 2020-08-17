from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from nvidia.models import *
from nvidia.utils import *
from rest_framework.validators import UniqueValidator
import copy


class ImageSerializerIn(serializers.ModelSerializer):
    #extra_fields = ExtraFieldContentSerializerOut(many=True)
    class Meta:
        model = ImageSegmentation
        fields = ('uuid', 'name', )


class ImageSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = ImageSegmentation
        fields = ('uuid', 'name','image_join','image_output','created_at', 'updated_at' )
