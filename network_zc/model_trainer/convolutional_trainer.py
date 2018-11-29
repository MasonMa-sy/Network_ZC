"""
For the first test to train neural networks for zc model using convolution layers.
"""
# Third-party libraries
from keras.layers import Input, Dense, Reshape, Flatten, Dropout, LeakyReLU, Conv2D, Conv2DTranspose, LocallyConnected2D
from keras import optimizers
from keras.models import Model
from keras.callbacks import TensorBoard
from keras import regularizers
from keras.layers.normalization import BatchNormalization
import keras.backend as K
from network_zc.keras_contrib.losses import DSSIMObjective
import numpy as np

# My libraries
from network_zc.tools import file_helper_unformatted, name_list, data_preprocess

# some initial parameter
model_name = name_list.model_name
data_preprocess_method = name_list.data_preprocess_method

training_start = 60
training_num = 12060
testing_num = 0
epochs = 50
batch_size = 64
kernel_size = name_list.kernel_size
max_value = name_list.max_value


def root_mean_squared_error(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1))


def mean_absolute_error(y_true, y_pred):
    return K.mean(K.abs(y_pred - y_true), axis=-1)


def mean_squared_error(y_true, y_pred):
    return K.mean(K.square(y_pred - y_true), axis=-1)


if __name__ == '__main__':
    # To define the model
    inputs = Input(shape=(20, 27, 2))
    layer1 = BatchNormalization()(inputs)
    # 20x27 to 8x12
    layer1 = Conv2D(filters=32, kernel_size=(4, 5), strides=2, padding='valid')(layer1)
    layer1 = BatchNormalization()(layer1)
    layer1 = LeakyReLU(alpha=0.3)(layer1)
    layer1 = Dropout(0.2)(layer1)
    # 9x12 to 7x10
    layer2 = Conv2D(filters=64, kernel_size=3, strides=1, padding='valid')(layer1)
    layer2 = BatchNormalization()(layer2)
    layer2 = LeakyReLU(alpha=0.3)(layer2)
    layer2 = Dropout(0.2)(layer2)
    # print(layer2.get_shape().as_list())
    layer3 = Flatten()(layer2)
    # layer3 = Dense(20*27, activation='linear')(layer3)
    # predictions = Reshape((20, 27, 1))(layer3)
    layer3 = Dense(7*10*64)(layer3)
    layer3 = BatchNormalization()(layer3)
    layer3 = LeakyReLU(alpha=0.3)(layer3)
    layer3 = Dropout(0.2)(layer3)
    layer3 = Reshape((7, 10, 64))(layer3)
    layer4 = Conv2DTranspose(filters=32, kernel_size=3, strides=1, padding='valid')(layer3)
    layer4 = BatchNormalization()(layer4)
    layer4 = LeakyReLU(alpha=0.3)(layer4)
    layer4 = Dropout(0.2)(layer4)
    predictions = Conv2DTranspose(filters=2, kernel_size=(4, 5), strides=2,
                                  padding='valid', activation='linear')(layer4)

    model = Model(inputs=inputs, outputs=predictions)
    # sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    adam = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
    ssim = DSSIMObjective(kernel_size=kernel_size, max_value=max_value)
    model.compile(optimizer=adam, loss=ssim,
                  metrics=[root_mean_squared_error, ssim, mean_absolute_error, mean_squared_error])
    # to train model
    # the data for training is ssta and ha
    training_data, testing_data = file_helper_unformatted.load_sstha_for_conv2d(training_start, training_num)

    # data preprocess z-zero
    if data_preprocess_method == 'preprocess_Z':
        training_data = data_preprocess.preprocess_Z(training_data, 0)
    # data preprocess dimensionless
    if data_preprocess_method == 'dimensionless':
        training_data = data_preprocess.dimensionless(training_data, 0)
    # data preprocess 0-1
    if data_preprocess_method == 'preprocess_01':
        training_data = data_preprocess.preprocess_01(training_data, 0)
    # data preprocess no month mean
    if data_preprocess_method == 'nomonthmean':
        training_data = data_preprocess.no_month_mean(training_data, 0)

    data_x = training_data[:-1]
    data_y = training_data[1:]
    tesorboard = TensorBoard('..\..\model\\tensorboard\\' + model_name)
    train_hist = model.fit(data_x, data_y, batch_size=batch_size, epochs=epochs, verbose=2,
                           callbacks=[tesorboard], validation_split=0.1)

    # To save the model and logs
    model.save('..\..\model\\' + model_name + '.h5')
    with open(file_helper_unformatted.find_logs(model_name+'_train'), 'w') as f:
        f.write(str(train_hist.history))
