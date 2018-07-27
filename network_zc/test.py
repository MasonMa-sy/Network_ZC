import numpy as np
from network_zc.tools import file_helper

# a = np.empty([540, 3])
# a[:, 0] = range(1, 541)
# a[:, 1] = 2 * a[:, 0]
# a[:, 2] = 3 * a[:, 0]
# print(a)
# b = np.reshape(a, (3, 1, 20, 27))
# print(b)
# a = np.empty(10)
# a[:] = range(1, 11)
# print(a)
# b = np.reshape(a, (5, 2), order='F')
# print(b)
# a = np.ones([27, 20])
# b = np.empty([27, 20, 2])
# b[:, :, 0] = a
# print(b)
test_data = file_helper.read_data_sstaha(0)
print(test_data)
