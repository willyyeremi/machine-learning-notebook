# library

# data analytic library
import pandas
import numpy

# visualization library
import matplotlib.pyplot

# machine learning
import sklearn.model_selection
import data_preparation
import missing_value
import ml_model

# loading data
data=data_preparation.load_data()

# preprocessing
missing_value.missing_value(a_data,b_data,feature_list)

# model
print(ml_model.multi_decision_tree(a_data,b_data,a_target,b_target,2,1000))