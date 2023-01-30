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
# data_description.data_description_1(data)

# choosing feature and target
# feature_target.numerical_feature(data)