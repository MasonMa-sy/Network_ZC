"""
This script is to plot the fig of loss
"""
# Third-party libraries
import matplotlib.pyplot as plt
import json
# My libraries
from network_zc.tools import file_helper
if __name__ == '__main__':
    with open(file_helper.find_logs('dense_model_train'), 'r') as file:
        data = file.read()
        history = json.loads(data.replace("'", '"'))
        # first subplot
        plt.subplot(2, 1, 1)
        plt.plot(history['val_loss'])
        plt.plot(history['loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['val', 'train'], loc='upper left')
        # second subplot
        plt.subplot(2, 1, 2)
        plt.plot(history['val_mean_squared_error'])
        plt.plot(history['mean_squared_error'])
        plt.title('model mae')
        plt.ylabel('mae')
        plt.xlabel('epoch')
        plt.legend(['val', 'train'], loc='upper left')

        plt.show()





