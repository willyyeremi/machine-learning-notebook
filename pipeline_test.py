import os
import sys
import importlib
import pandas

for folder in os.listdir(os.getcwd()+r"\src"):
    sys.path.insert(0,os.getcwd()+"\\src\\"+folder)
    module_list=[]
    for cust_module in os.listdir(os.getcwd()+r"\src\\"+folder):
        if cust_module.endswith(".py"):
            x=cust_module.removesuffix('.py')
            module_list.append(x)
    for lib in module_list:
        globals()[lib] = importlib.import_module(lib)

# write the path of the data bellow
path=r"C:\Users\willy\Documents\Database\Kaggle\Melbourne Housing Snapshot\melb_data.csv"

# choose option of your data
# 1: only single file data
# 2: multiple data from folder
type_data=1

# loading data
data=load_data.load_data(path,type_data)

# data information
data_information.data_description(data)

# for data with int64 or float64 type
numerical_feature=["Rooms","Bedroom2","Bathroom","Car","Landsize","BuildingArea"]

# for categorical data with ordinality
oe_feature=["Type"]

# for categorical data without ordinality and <=10 categories
ohe_feature=["Regionname"]

# for categorical data without ordinality and >10 categories
te_feature=["CouncilArea"]

# for data that will get predicted
target=["Price"]

# checking feature
nf=feature_target.numerical_check(data,numerical_feature)
cf=feature_target.categorical_check(data,oe_feature,ohe_feature,te_feature)
if len(cf)>0:
    feature=nf+cf
else:
    feature=nf

# processing feature
feature=data[feature]
target=data[target]

# sample of feature and target
print(feature)
print(target)

# how you will divide the data. put the number of the option inside the paranthesis
# 1: random
# 2: determined by you
# 3: cross validation
split_type=[2]

# fill this variable if you choose option 2 or 3. write inside the paranthesis.
# 1. if you choose option 2, fill it with train set and test set. format (train set ratio,test set ratio)
# 2. if you choose option 3, fill it with how many fold you want the validation get done. format (number of fold)
variable_split=[8,2]

# splitting dataset
train_data,train_target,test_data,test_target=splitting_method.method_selector(split_type,variable_split,feature,target)

# sample of train and test set
print(train_data)
print(train_target)
print(test_data)
print(train_target)

