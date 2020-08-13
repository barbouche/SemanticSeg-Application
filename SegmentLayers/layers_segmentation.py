
import torch.nn as nn
import torch.nn.functional as F
from collections import OrderedDict


class _SimpleSegmentationModel(nn.Module):
    """
    Implements the primary layers for the DeepLab v3 architecture
    """
    def __init__(self, backbone, classifier):
        super(_SimpleSegmentationModel, self).__init__()
        self.backbone = backbone
        self.classifier = classifier

    def forward(self, x):
        input_shape = x.shape[-2:]
        features = self.backbone(x)
        x = self.classifier(features)
        x = F.interpolate(x, size=input_shape, mode='bilinear', align_corners=False)
        return x

class LayerPicker(nn.ModuleDict):
    """
    Module wrapper that returns specific layers from a priorly
    implemented model. In this case takes the needed layers involved in the DeepLab backbone
    Arguments:
        ModuleDict: The model to extract the features from
    Returns:
        Dict: Dictionary with the desired layers extracted
    Example:
        model = DeepLabV3(pretrained=True)
        extracted_model = LayerPicker(model, {'layer1':'feature1', 'layer2': 'feature2'})
        tensor = torch.tensor(1, 3, 224, 224)
        output = extracted_model(tensor)
        print([(k, v.shape) for k, v in output.items])
         "feature1": torch.size(1, 3, 65, 65)
         "feature2": torch.size(1, 3, 24, 24)
    """
    def __init__(self, model, return_layers):
        if not set(return_layers).issubset([name for name, _ in model.named_children()]):
            raise ValueError("specified layers not present in the model")

        orig_return_layers = return_layers
        return_layers = {k: v for k, v in return_layers.items()}
        layers = OrderedDict()
        for name, module in model.named_children():
            layers[name] = module
            if name in return_layers:
                del return_layers[name]
            if not return_layers:
                break

        super(LayerPicker, self).__init__(layers)
        self.return_layers = orig_return_layers

    def forward(self, x):
        out = OrderedDict()
        for name, module in self.named_children():
            x = module(x)
            if name in self.return_layers:
                out_name = self.return_layers[name]
                out[out_name] = x
        return out
