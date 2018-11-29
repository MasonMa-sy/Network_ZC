"""

"""
# Third-party libraries
from keras.layers import Input, Dense
from keras import optimizers
from keras.models import Model
from keras.callbacks import TensorBoard
import numpy as np
from keras.models import load_model
import keras.backend as K
import matplotlib.pyplot as plt
# My libraries
from network_zc.tools import file_helper_unformatted, data_preprocess, name_list
from network_zc.tools import index_calculation
from network_zc.model_trainer import dense_trainer
from network_zc.model_trainer import dense_trainer_sstaha
from network_zc.model_trainer import dense_trainer_sstaha_4
from network_zc.model_trainer import convolutional_trainer_alex


def root_mean_squared_error(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1))


def mean_absolute_error(y_true, y_pred):
    return K.mean(K.abs(y_pred - y_true), axis=-1)


def mean_squared_error(y_true, y_pred):
    return K.mean(K.square(y_pred - y_true), axis=-1)


if __name__ == '__main__':
    # Load the model
    model_name = name_list.model_name
    retrain_model_name = name_list.retrain_model_name
    model = load_model('..\model\\' + model_name + '.h5', custom_objects={'mean_squared_error': mean_squared_error
    , 'root_mean_squared_error': root_mean_squared_error, 'mean_absolute_error': mean_absolute_error})
    print(len(model.layers))
    training_start = 0
    all_num = 464
    batch_size = 32
    epochs = 200
    data_preprocess_method = name_list.data_preprocess_method

    all_data, testing_data = file_helper_unformatted.load_sstha_for_conv2d(training_start, all_num)
    # data preprocess z-zero
    if data_preprocess_method == 'preprocess_Z':
        all_data = data_preprocess.preprocess_Z(all_data, 0)
    # data preprocess dimensionless
    if data_preprocess_method == 'dimensionless':
        all_data = data_preprocess.dimensionless(all_data, 0)
    # data preprocess 0-1
    if data_preprocess_method == 'preprocess_01':
        all_data = data_preprocess.preprocess_01(all_data, 0)
    # data preprocess no month mean
    if data_preprocess_method == 'nomonthmean':
        all_data = data_preprocess.no_month_mean(all_data, 0)

    data_x = np.reshape(all_data[:-1], (all_num, 1080))
    data_y = np.reshape(all_data[1:], (all_num, 1080))

    for layer in model.layers[:]:
        layer.trainable = False
    for layer in model.layers[6:10]:
        layer.trainable = True
    for layer in model.layers:
        print(layer.trainable)
    adam = optimizers.Adam(lr=0.00001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
    model.compile(optimizer=adam, loss=mean_squared_error, metrics=[mean_squared_error, root_mean_squared_error,
                                                                    mean_absolute_error])
    tesorboard = TensorBoard('..\model\\tensorboard\\' + retrain_model_name)
    train_hist = model.fit(data_x, data_y, batch_size=batch_size, epochs=epochs, verbose=2,
                           callbacks=[tesorboard], validation_split=0.1)
    model.save('..\model\\' + retrain_model_name + '.h5')
    with open('..\model\\logs\\'+retrain_model_name + '_train', 'w') as f:
        f.write(str(train_hist.history))
