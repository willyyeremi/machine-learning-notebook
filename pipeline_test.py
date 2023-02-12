import os
import sys
import importlib
import pandas
import sklearn.model_selection

for folder in os.listdir(os.getcwd()+r"\src"):
    sys.path.insert(0,os.getcwd()+"\\src\\"+folder)
    module_list=[]
    for cust_module in os.listdir(os.getcwd()+r"\src\\"+folder):
        if cust_module.endswith(".py"):
            x=cust_module.removesuffix('.py')
            module_list.append(x)
    for lib in module_list:
        globals()[lib] = importlib.import_module(lib)

# loading data
data=pandas.read_csv(r"C:\Users\willy\Documents\Database\Kaggle\Melbourne Housing Snapshot\melb_data.csv")

# # data information
data_information.data_description(data)


# for data with int64 or float64 type
numerical_feature=["Rooms","Bedroom2","Bathroom","Car","Landsize","BuildingArea"]

# for categorical data with ordinality
ordinal_feature=["Type"]

# for categorical data without ordinality and <=10 categories
oh_feature=["Regionname"]

# for categorical data without ordinality and >10 categories
target_feature=["CouncilArea"]

# for data that will get predicted
target=["Price"]


# checking feature
nf=feature_target.numerical_feature(data,numerical_feature)
cf=feature_target.categorical_check(data,ordinal_feature,oh_feature,target_feature)
if len(cf)>0:
    feature=nf+cf
else:
    feature=nf

# processing feature
feature=data[feature]
target=data[target]

# how you will divide the data. put the number of the option inside the paranthesis
# 1: random
# 2: determined by you
# 3: cross validation
split_type=[2]

# fill this variable if you choose option 2 or 3. write inside the paranthesis.
# 1. if you choose option 2, fill it with train set and test set. format (train set ratio,test set ratio)
# 2. if you choose option 3, fill it with how many fold you want the validation get done. format (number of fold)
variable_split=[8,2]

train_data,train_target,test_data,test_target=splitting_method.method_selector(split_type,variable_split,feature,target)

