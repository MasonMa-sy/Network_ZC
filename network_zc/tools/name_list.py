"""
This script is for some parameter set.
"""
# for model
model_name = 'conv_model_dimensionless_1_ZC_sc_1#mae_bs4'
model_type = 'conv'
# for retrain model, because ZC data and observation data are symmetrical with the equator
is_retrain = False
retrain_model_name = 'conv_model_dimensionless_1_ZC_sc_1_to_historical_5'
# for continue model
continue_model_name = 'conv_model_dimensionless_1_historical_sc_small@best'
# for ssim
kernel_size = 7
max_value = 10
# for seasonal circle
is_seasonal_circle = True
# for final essay
is_best = False

# for reading data
data_file = 'data_nature2'
data_name = '\data_'
# data_file = 'data_historical'
# data_name = '\data_historical_'
# data_file = 'data_test'
# data_name = '\predict_data_'
# data_file = 'data_predict_0'
# data_name = '\data_'
# for data preprocess
data_file_statistics = '..\data\predict_data_'
data_preprocessing_file = '\mean\\'
# for historical_data_interpolate
data_historical_file = '\historical_data\\'
historical_binary_file = 'data_historical\data_wind'


# for data preprocess
data_preprocess_method = 'dimensionless'
