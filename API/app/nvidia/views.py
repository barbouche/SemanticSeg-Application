from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.cache import cache_page, never_cache
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import requests
from nvidia.models import *
from nvidia.serializers import *
import json
import os
import re
from .utils import *
from dependencies.scripts_male_voice import *
from django.apps import apps
from django.conf import settings
from django.http import FileResponse
import time
import numpy as np
#from torch.models import resnet18 as _resnet18
from pydub import AudioSegment

import speech_recognition as sr
import librosa
#from nvidia.models_manager import ModelsManager
#from scripts.init import modelManager, PARAMETERS_MODEL
from app.apps import ModelConfig
from django.http import HttpResponseNotFound



BASE_DIR = settings.BASE_DIR
MEDIA_ROOT = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL
MEDIA_TEMP_DIR = os.path.join(MEDIA_ROOT,'temp/')
#PARAMETERS_MODEL = settings.PARAMETERS_MODEL



@api_view(['GET'])
@never_cache
def test_api_communication(request):
    """
    ** To enable actions you should get valid Token


    ** Use Case Exemple of Post:

        Just make empty request


    """
    "testing some paramater"

    return Response({'response':"Congra, you are connected to Nvidia API!"})



@api_view(['POST'])
@never_cache
def image_segmentation(request):
    """
    ** Create new image segmentation to convert background to black .
    ** Use Case Exemple of Post:
                    {
                        "image":binary base64,
                    }
    Required:

    image

    """
    file_ = request.FILES['image']
    image = ImageSegmentation.objects.create(image_join =file_, name='image_%02d' % uuid.uuid1())
    segmentation_inference(image)
    serializer = ImageSerializerOut(image)
    return Response( serializer.data )
