import sys
import pandas
import sklearn.model_selection

sys.path.insert(0,"C:/Users/willy/Documents/GitHub/test-machine-learning/data_preparation")
sys.path.insert(0,"C:/Users/willy/Documents/GitHub/test-machine-learning/preprocessing")
sys.path.insert(0,"C:/Users/willy/Documents/GitHub/test-machine-learning/model")
import data_description
import feature_target
import missing_value
import multi_decision_tree

# loading data
data=pandas.read_csv(r"C:\Users\willy\Documents\Database\Kaggle\Melbourne Housing Snapshot\melb_data.csv")

# data information
data_description.data_description_1(data)



# # for data with int64 or float64 type
# numerical_feature=["Rooms","Bedroom2","Bathroom","Car","Landsize"]

# # for categorical data with ordinality
# ordinal_feature=[]

# # for categorical data without ordinality and <=10 categories
# oh_feature=[]

# # for categorical data without ordinality and >10 categories
# target_feature=[]

# # for data that will get predicted
# target=["Price"]

# # checking feature
# nf=feature_target.numerical_feature(data,numerical_feature)
# cf=feature_target.categorical_check(data,ordinal_feature,oh_feature,target_feature)
# if len(cf)>0:
#     feature=nf.append(cf)
# else:
#     feature=nf

# # processing feature
# feature=data[feature]
# target=data[target]

# print(feature)
# print(target)