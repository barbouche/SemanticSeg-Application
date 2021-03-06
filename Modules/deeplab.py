
import torch
import torch.nn as nn
import numpy as np
import cv2
import torchvision.models.segmentation as models
from Dataset.image_data import SegmentationSample
from BackBones.resnet_calls import load_resnet_101
from DeepLabV3Implementation.deeplab_implementation import DeepLabHead, DeepLabV3
from SegmentLayers.layers_segmentation import

class SemanticSeg(nn.Module):
    def __init__(self, pretrained: bool, device):
        super(SemanticSeg, self).__init__()
        if device == 'cuda' and torch.cuda.is_available():
            self.device = 'cuda'
        if device == 'cpu':
            self.device = 'cpu'

        self.model = self.load_model(pretrained)

    def __getitem__(self, item):
        return self.model

    def load_deeplab_implementation(self, backbone_name, output_stride, pretrained=False):
        if output_stride == 8:
            replace_stride_with_dilation = [False, True, True]
            aspp_dilate = [12, 24, 36]
        else:
            replace_stride_with_dilation = [False, False, True]
            aspp_dilate = [6, 12, 18]

    # Add the Backbone option in the parameters
    def load_model(self, output_stride, pretrained_backbone):
        if output_stride == 8:
            replace_stride_with_dilation = [False, True, True]
            aspp_dilate = [12, 24, 36]
        else:
            replace_stride_with_dilation = [False, False, True]
            aspp_dilate = [6, 12, 18]

        backbone = load_resnet_101(replace_stride_with_dilation)
        inplanes = 2048
        low_level_planes = 256

        # DeepLab V3 version
        return_layers = {'layer4': 'out'}
        classifier = DeepLabHead(inplanes, 21, aspp_dilate)
        backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)

        model.to(self.device)
        # dummy_input = torch.randn(1, 3, 224, 224, dtype=torch.float).to(self.device)
        # starter, ender = torch.cuda.Event(enable_timing=True)
        # repetitions = 300
        # timings = np.zeros((repetitions, 1))
        # # GPU-WARM-UP
        # for _ in range(10):
        #     _ = model(dummy_input)
        model.eval()
        return model

    def run_inference(self, image: SegmentationSample):
        # Run the model in the respective device:
        with torch.no_grad():
            output = self.model(image.processed_image)['out']

        reshaped_output = torch.argmax(output.squeeze(), dim=0).detach().cpu().numpy()
        return self.decode_segmentation(reshaped_output, image.image_file)


    def decode_segmentation(self, input_image, source, number_channels=21):

        label_colors = np.array([(0, 0, 0),  # 0=background
                                 # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
                                 (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
                                 # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
                                 (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0),
                                 # 11=dining table, 12=dog, 13=horse, 14=motorbike, 15=person
                                 (192, 128, 0), (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128),
                                 # 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor
                                 (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128)])

        # Defining empty matrices for rgb tensors:
        r = np.zeros_like(input_image).astype(np.uint8)
        g = np.zeros_like(input_image).astype(np.uint8)
        b = np.zeros_like(input_image).astype(np.uint8)

        for l in range(0, number_channels):
            if l == 15:
                idx = input_image == l
                r[idx] = label_colors[l, 0]
                g[idx] = label_colors[l, 1]
                b[idx] = label_colors[l, 2]

        rgb = np.stack([r, g, b], axis=2)
        # return rgb

        foreground = cv2.imread(source)

        # and resize image to match shape of R-band in RGB output map
        foreground = cv2.resize(foreground, (r.shape[1], r.shape[0]))
        foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB)

        background = 0 * np.ones_like(rgb).astype(np.uint8)

        foreground = foreground.astype(float)
        background = background.astype(float)

        # Create a binary mask using the threshold
        th, alpha = cv2.threshold(np.array(rgb), 0, 255, cv2.THRESH_BINARY)

        # Apply Gaussian blur to the alpha channel
        alpha = cv2.GaussianBlur(alpha, (7, 7), 0)
        alpha = alpha.astype(float) / 255

        foreground = cv2.multiply(alpha, foreground)
        background = cv2.multiply(1.0 - alpha, background)

        outImage = cv2.add(foreground, background)

        return outImage / 255

