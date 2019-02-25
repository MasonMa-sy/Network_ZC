"""
This script is for some parameter set.
"""
# for model
model_name = 'conv_model_dimensionless_1_historical_sc'
model_type = 'conv'
# for retrain model
is_retrain = False
retrain_model_name = 'conv_model_dimensionless_to_historical_test_1'
# for continue model
continue_model_name = 'conv_model_dimensionless_to_historical_test_1'
# for ssim
kernel_size = 7
max_value = 10
# for seasonal circle
is_seasonal_circle = True

# for reading data
data_file = 'data_historical'
data_name = '\data_historical_'
# for data preprocess
data_file_statistics = '..\data\predict_data_'
data_preprocessing_file = '\mean\\'
# for historical_data_interpolate
data_historical_file = '\historical_data\\'
historical_binary_file = 'data_historical\data_wind'


# for data preprocess
data_preprocess_method = 'dimensionless'
