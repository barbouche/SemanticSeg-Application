from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, m2m_changed, pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.dispatch import receiver
from django.db.models import Q, F, Max
from django.db.models import Count, Case, When, IntegerField
from django.utils.safestring import mark_safe
import uuid
import os
import re
from django.contrib.contenttypes.models import ContentType
from nvidia.utils import  get_path_image, get_path_media_audio_transformation, get_path_image_output,get_path_media
from datetime import datetime, timedelta
from collections import OrderedDict
from jsonfield import JSONField
from django.contrib.gis.geos import Point
from datetime import date
from dateutil.relativedelta import relativedelta
import treepoem
import base64
from io import BytesIO
import string
import numpy as np
from django.conf import settings
#from users.models import *
from django.contrib.postgres.fields.array import ArrayField
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pprint
import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
import datetime

BASE_DIR = settings.BASE_DIR
MEDIA_ROOT = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL



class ImageSegmentation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,null=True, blank=True)
    image_join = models.FileField(upload_to=get_path_image, null=True, blank=True)
    image_output = models.FileField(upload_to=get_path_image_output, null=True, blank=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "ImageSegmentation"
        verbose_name_plural = "ImageSegmentations"

    def __str__(self):
        return "%s" % self.name
