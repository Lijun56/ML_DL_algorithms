import numpy as np


def train_test_split(X, y, test_ration = 0.2, seed=None):
  assert X.shape[0] == y.shape[0], \
    "the size of x must be equal to the size of y"
  assert 0.0 <= test_ration <= 1.0, \
    "ration of test data must be valid"
#   The seed parameter ensures reproducibility.
#  Setting np.random.seed(seed) makes the train-test split consistent across runs by fixing the shuffle order of indices. This is useful for getting the same split each time the function is called with the same seed.
  if seed:
    np.random.seed(seed)

  # random the indexs within len(x)
  shuffle_indexes = np.random.permutation(len(X))

  test_size = int(len(X) * test_ration)
  test_indexes = shuffle_indexes[:test_size]
  train_indexes = shuffle_indexes[test_size:]

  x_train = X[train_indexes]
  y_train = y[train_indexes]

  x_test = X[test_indexes]
  y_test = y[test_indexes]

  return x_train, x_test, y_train, y_test