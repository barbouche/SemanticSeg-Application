
import torch
from .resnet import ResNet, Bottleneck
import torchvision.models.utils as models

resnet_model_url = 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth'

def load_resnet_state_dict(block, layers, pretrained, progress, **kwargs):
    model = ResNet(block, layers, **kwargs)
    state_dict = models.load_state_dict_from_url(resnet_model_url, progress=progress)
    model.load_state_dict(state_dict)

    return model

def load_resnet_101(progress=True, **kwargs):
    """
    Loads Resnet_101 pretrained on ImageNet as a Backbone for DeepLab
    :param pretrained: Returns pretrained resnet_101 on ImageNet
    :param progress: Show download progress
    :param kwargs: other additional params
    :return: resnet_101 model used as Backbone for DeepLab V3
    """
    return load_resnet_state_dict(Bottleneck, [3, 4, 23, 3], progress, **kwargs)

