def random(feature,target):
    '''use train test split from sklearn'''
    import sklearn.model_selection
    train_data,train_target,test_data,test_target=sklearn.model_selection.train_test_split(feature,target,random_state=1)
    return train_data,train_target,test_data,test_target