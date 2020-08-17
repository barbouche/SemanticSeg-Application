# This is a sample Python script.
import torch
import torchvision.models.segmentation as models
import matplotlib.pyplot as plt
from torchvision import transforms
from PIL import Image
import torch
from torchvision.models.segmentation.deeplabv3 import DeepLabV3
import cv2
import numpy as np
from Dataset.image_data import SegmentationSample
from Modules.deeplab import SemanticSeg





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    PATH = 'C:\\Users\\ayman\\OneDrive\\Documents\\Instance Segmentation\\Images\\Test Images Skype Stream Part 1\\Person-2-sample'
    image = SegmentationSample(root_dir=PATH, image_file='display3.jpeg', device='cpu')

    # Bonjour

    #image.print_processed()
    # A small change here
    #model = SemanticSeg(pretrained=True, device='cpu')
    #res = model.run_inference(image)

    #plt.imshow(res)
    #plt.pause(5)
    #plt.figure()

    # PATH = 'C:\\Users\\ayman/.cache/torch\\hub\\checkpoints\\deeplabv3_resnet101_coco-586e9e4e.pth'
    # model = models.deeplabv3_resnet101(pretrained=True)
    # model.eval()
    # print(model)

    # Getting the images:
    # image_path = './photo-test1.jpeg'
    # image = Image.open(image_path)
    # # image = image.convert('RGB')
    #
    # input_process = transforms.Compose([
    #     transforms.ToTensor(),
    #     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    #
    # processed_image = input_process(image).unsqueeze(0)
    # unload_image = transforms.ToPILImage()
    # new_image = processed_image.squeeze(0)
    # new_image = unload_image(new_image)
    #
    # input_img2 = Image.open(image_path)
    # input_tensor = input_process((input_img2))
    # input_batch = input_tensor.unsqueeze(0)
    #
    # if torch.cuda.is_available():
    #     print('yes')
    #     input_batch = input_batch.to('cuda')
    #     model.to('cuda')
    #
    # with torch.no_grad():
    #     output = model(input_batch)['out']
    #
    # reshaped_output = torch.argmax(output.squeeze(), dim=0).detach().cpu().numpy()
    # result = decode_segmentation(reshaped_output, image_path)
    #
    #
    # plt.imshow(result)
    # plt.pause(10)
    # plt.figure()
