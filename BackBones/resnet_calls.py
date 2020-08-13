
import torch
from .resnet import ResNet
from torchvision.models.utils import load_state_dict_from_url

def load_resnet_state_dict(model_arch, block, layers, progress, **kwargs):
    model = ResNet(block, layers, **kwargs)
    state_dict = load_state_dict_from_url()