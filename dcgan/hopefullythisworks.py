
from keras.models import model_from_yaml
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

yaml_file = open(os.path.abspath(os.path.dirname(sys.argv[0]))+'/model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights(os.path.abspath(os.path.dirname(sys.argv[0]))+"/gen.h5")
print(loaded_model.summary())
control_im = np.random.normal(size = (1, 32)) / 2
gen_im = loaded_model.predict(control_im)
im = Image.fromarray(np.uint8(gen_im[0, :, :, :] * 255))
im.save(os.path.abspath(os.path.dirname(sys.argv[0]))+"/resultImg/123.jpg")
print("Done bitches!!")