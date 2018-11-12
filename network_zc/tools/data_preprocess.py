"""
This script is done for data preprocess
"""

# Third-party libraries
import numpy as np
import struct
# My libraries
from network_zc.tools import file_helper_unformatted

data_file = file_helper_unformatted.data_file
data_name = file_helper_unformatted.data_name
data_file_statistics = file_helper_unformatted.data_file_statistics
data_preprocessing_file = file_helper_unformatted.data_preprocessing_file

def read_preprocessing_data():
    """

    :return: mean data and std data for data preprocessing.
    """
    filename = "D:\msy\projects\zc\zcdata\\" + data_file + data_preprocessing_file + "mean.dat"
    fh = open(filename, mode='rb')
    data_mean = np.empty([20, 27, 2])
    for i in range(20):
        for j in range(27):
            data = fh.read(8)  # type(data) === bytes
            text = struct.unpack("d", data)[0]
            data_mean[i][j][0] = text
    for i in range(20):
        for j in range(27):
            data = fh.read(8)  # type(data) === bytes
            text = struct.unpack("d", data)[0]
            data_mean[i][j][1] = text
    fh.close()
    filename = "D:\msy\projects\zc\zcdata\\" + data_file + data_preprocessing_file + "std.dat"
    fh = open(filename, mode='rb')
    data_std = np.empty([20, 27, 2])
    for i in range(20):
        for j in range(27):
            data = fh.read(8)  # type(data) === bytes
            text = struct.unpack("d", data)[0]
            data_std[i][j][0] = text
    for i in range(20):
        for j in range(27):
            data = fh.read(8)  # type(data) === bytes
            text = struct.unpack("d", data)[0]
            data_std[i][j][1] = text
    fh.close()
    return data_mean, data_std


def preprocess(training_data):
    """
    for Z-score normalization
    :param training_data:
    :return:
    """
    data_mean, data_std = read_preprocessing_data()
    training_data = (training_data - data_mean) / data_std
    return training_data


def preprocess2_for_train(training_data):
    training_min0 = training_data[:, :, :, 0].min()
    training_max0 = training_data[:, :, :, 0].max()
    training_min1 = training_data[:, :, :, 1].min()
    training_max1 = training_data[:, :, :, 1].max()
    filename = "D:\msy\projects\zc\zcdata\\" + data_file + data_preprocessing_file + "MaxMin.dat"
    fh = open(filename, mode='wb')
    data = struct.pack("d", training_min0)
    fh.write(data)
    data = struct.pack("d", training_max0)
    fh.write(data)
    data = struct.pack("d", training_min1)
    fh.write(data)
    data = struct.pack("d", training_max1)
    fh.write(data)
    fh.close()


def preprocess2(training_data, di_or_de):
    """
    for 0-1 normalization
    :param di_or_de:
    :param training_data:
    :return:
    """
    filename = "D:\msy\projects\zc\zcdata\\" + data_file + data_preprocessing_file + "MaxMin.dat"
    fh = open(filename, mode='rb')
    data = fh.read(8)
    training_min0 = struct.unpack("d", data)[0]
    data = fh.read(8)
    training_max0 = struct.unpack("d", data)[0]
    data = fh.read(8)
    training_min1 = struct.unpack("d", data)[0]
    data = fh.read(8)
    training_max1 = struct.unpack("d", data)[0]
    fh.close()
    # print("%g!%g!%g!%g" % (training_min0, training_max0, training_min1, training_max1))
    if di_or_de == 0:
        training_data[:, :, :, 0] = (training_data[:, :, :, 0] - training_min0) / (training_max0 - training_min0)
        training_data[:, :, :, 1] = (training_data[:, :, :, 1] - training_min1) / (training_max1 - training_min1)
    if di_or_de == 1:
        training_data[:, :, :, 0] = training_data[:, :, :, 0] * (training_max0 - training_min0) + training_min0
        training_data[:, :, :, 1] = training_data[:, :, :, 1] * (training_max1 - training_min1) + training_min1
    return training_data


def dimensionless(training_data, di_or_de):
    """
    ssta/2, h1a/50
    :param training_data:
    :param di_or_de:0 for many sample /, 1 for many sample *.
    :return:
    """
    if di_or_de == 0:
        training_data[:, :, :, 0] = training_data[:, :, :, 0] / 2
        training_data[:, :, :, 1] = training_data[:, :, :, 1] / 50
    if di_or_de == 1:
        training_data[:, :, :, 0] = training_data[:, :, :, 0] * 2
        training_data[:, :, :, 1] = training_data[:, :, :, 1] * 50
    return training_data
