"""
This script is for some parameter set.
"""
# for model
model_name = 'conv_model_dimensionless_2_ssim'
model_type = 'conv'
# for retrain model
retrain_model_name = 'dense_model_dimensionless_to_historical'
# for ssim
kernel_size = 3
max_value = 10

# for reading data
data_file = 'data_nature2'
data_name = '\data_'
# for data preprocess
data_file_statistics = '..\data\predict_data_'
data_preprocessing_file = '\mean\\'
# for historical_data_interpolate
data_historical_file = '\historical_data\\'
historical_binary_file = 'data_historical'


# for data preprocess
data_preprocess_method = 'dimensionless'
