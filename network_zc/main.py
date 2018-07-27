"""

"""
# Third-party libraries
from keras.layers import Input, Dense
from keras import optimizers
from keras.models import Model
import numpy as np
from keras.models import load_model
# My libraries
from network_zc.tools import file_helper
from network_zc.model_trainer import dense_trainer
from network_zc.model_trainer import convolutional_trainer

# Load the model
model_name = convolutional_trainer.model_name
model = load_model('..\model\\' + model_name + '.h5')

# Predict
# file_num = np.arange(3100, 3400, 30)
# for x in file_num:
#     predict_data = np.empty([1, 540])
#     predict_data[0] = data_loader.read_data(x)
#     data_loader.write_data(x, model.predict(predict_data)[0])
file_num = 4793
# predict_data = np.empty([1, 540])
# predict_data[0] = file_helper.read_data(file_num)
# file_helper.write_data(file_num, model.predict(predict_data)[0])
predict_data = np.empty([1, 540])
predict_data[0] = file_helper.read_data(file_num)
predict_result = model.predict(np.reshape(predict_data[0], (1, 20, 27, 1)))
file_helper.write_data_conv2d(file_num, predict_result[0])
