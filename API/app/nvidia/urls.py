
from django.urls import path, include, re_path
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from nvidia.views import *

app_name='nvidia'

urlpatterns = [
    #path(r'text_to_speech_female/', text_to_speech, name='text_to_speech'),
    #path(r'text_to_speech_male/', text_to_speech_male, name='text_to_speech_male'),
    path(r'test/', test_api_communication, name='test_api_communication'),
    path(r'image_segmentation/', image_segmentation, name='image_segmentation'),



]
