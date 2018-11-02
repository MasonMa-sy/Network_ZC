from network_zc.model_trainer.dense_trainer_sstaha_3 import get_testing_index
from network_zc.tools import file_helper
import numpy as np

training_num = 3000
training_num2 = 12000

# training_data, testing_data = file_helper.load_sstha_for_conv2d(training_num-1)
# data_y = np.reshape(training_data[get_testing_index(training_num), :, :, 0], (training_num2, 540))
# data_mean = np.mean(data_y, axis=0)
# file_helper.write_data(0, data_mean)

training_data, testing_data = file_helper.load_sstha_for_conv2d_separate(training_num)
data_y = np.reshape(testing_data[:, :, :, 0], (training_num, 540))
data_mean = np.mean(data_y, axis=0)
file_helper.write_data(1, data_mean)
