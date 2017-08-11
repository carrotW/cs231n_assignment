import random
import numpy as np
# from cs231n.data_utils import load_CIFAR10
# import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize'] = (10.0,8.0)
#
# # load the raw CIFAR-10 data
# cifar10_dir = "cs231n/datasets/cifar-10-batches-py"
# x_train, y_train, x_test, y_test = load_CIFAR10(cifar10_dir)
#
# print "Training data shape: ", x_train.shape

X = np.array([0,1,2,3,4,5])
Y = np.array([0,1,2,3,4,5,6,7,8])
dists = np.zeros((6, 9))
dists2 = np.zeros((6, 9))
dists3 = np.zeros((6, 9))
for i in xrange(6):
    for j in xrange(9):
        dists[i,j] = np.linalg.norm(X[i]-Y[j])
# print(dists)
# print(np.sum(dists))
# for i in xrange(6):
#     dists2[i] = np.linalg.norm(X[i]-Y)
#     print dists2[i]

# print(X * np.reshape(Y, (9,1)))
# print(X+Y)
# print np.array_split(Y, 2)
ktoacc = {}
ktoacc[12]=3.233
# print ktoacc
li = [1,2,3,4,5,6,7,8]
li.pop(2)
print li