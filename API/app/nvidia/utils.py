import re
import os
import sys
import numpy as np
#from scipy.io.wavfile import write
#import torch
#from IPython.display import Audio
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext
import re
import os
import sys
import uuid
from functools import wraps
from datetime import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from nvidia.models import *
import numpy as np
from IPython.display import Audio
from playsound import playsound
import torch
from scipy.io.wavfile import write
from IPython.display import Audio
from pydub import AudioSegment
import ffmpy
import ffmpeg

from app.apps import ModelConfig
import IPython.display as ipd
import librosa

import torchvision.models.segmentation as models
import matplotlib.pyplot as plt
from torchvision import transforms
from PIL import Image
import torch
from torchvision.models.segmentation.deeplabv3 import DeepLabV3
import cv2

from dependencies.computer_vision.Dataset.image_data import SegmentationSample
from dependencies.computer_vision.Modules.deeplab import SemanticSeg

def get_path_media(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'media/audio/{}{}'.format(uuid.uuid4(), ext)


def get_path_image(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'media/image/{}{}'.format(uuid.uuid4(), ext)

def get_path_image_output(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'media/image_output/{}{}'.format(uuid.uuid4(), ext)

def get_path_media_audio_transformation(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'audio_transformation/{}{}'.format(uuid.uuid4(), ext)


def segmentation_inference(image_):
    fixed_path = "media/image_output/"
    base_path, filename = os.path.split(image_.image_join.path)
    image = SegmentationSample(root_dir=base_path, image_file=filename, device='cuda')
    model = SemanticSeg(pretrained=True, device='cuda')
    res = model.run_inference(image)
    image_to_array =Image.fromarray((res * 255).astype(np.uint8))
    image_to_array.save(fixed_path+ filename )
    image_.image_output=fixed_path+ filename
    image_.save()
