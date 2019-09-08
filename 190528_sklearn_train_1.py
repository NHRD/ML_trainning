from sklearn import datasets
from sklearn import svm
from sklearn import metrics
import matplotlib.pyplot as plt

digits = datasets.load_digits()

print(dir(digits))