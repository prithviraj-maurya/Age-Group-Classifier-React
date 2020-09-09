import io
import numpy as np
import torch

from torch import nn
import torch.utils.model_zoo as model_zoo
import torch.onnx

import onnx
import onnxruntime
from PIL import Image
import torchvision.transforms as transforms

model_file = 'age-group-clf_pretrained_resnet.onnx'

onnx_model = onnx.load(model_file)
onnx.checker.check_model(onnx_model)



ort_session = onnxruntime.InferenceSession(model_file)

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

sample_img = Image.open('download.jpeg')


resize = transforms.Resize([250, 250])
to_tensor = transforms.ToTensor()
sample_image = resize(sample_img)
sample_image = np.float32(np.array(sample_image, dtype=float))
sample_image = np.moveaxis(sample_image, -1, 0)
sample_image = torch.from_numpy(sample_image)
sample_image = sample_image[np.newaxis, :] 

ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(sample_image)}
ort_outs = ort_session.run(None, ort_inputs)
print(f'Output: {ort_outs}')