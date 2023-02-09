def random(feature,target):
    '''use train test split from sklearn'''
    import sklearn.model_selection
    train_data,train_target,test_data,test_target=sklearn.model_selection.train_test_split(feature,target,random_state=1)
    return train_data,train_target,test_data,test_target

def self_determine(feature,target,ratio):
    '''divide between train and test with ratio'''
    import pandas
    if len(ratio)!=2:
        print("the ratio filling of ratio variable is not following the format. please check again.")
        return None,None,None,None
    elif len(ratio)==2:
        for x in ratio:
            if isinstance(x,int)!=True:
                print("please fill the variable_split only with int type data")
                return None,None,None,None
        if ratio[0]<ratio[1]:
            print("the train set proportion is smaller then test set. please check again.")
            return None,None,None,None
        else:
            total_row=feature.shape[0]
            total_ratio=ratio[0]+ratio[1]
            train_data=feature[:(total_row//total_ratio*ratio[0])]
            train_target=target[:(total_row//total_ratio*ratio[0])]
            test_data=feature[(total_row//total_ratio*ratio[0]+1):]
            test_target=target[(total_row//total_ratio*ratio[0]+1):]
            return train_data,train_target,test_data,test_target

def cross_val(feature,target,option_2):
    '''function to refer to cross_val module'''
    import cross_val
    cross_val.cross_val(feature,target,option_2)

def method_selector(option_1,option_2,feature,target):
    '''selector for choosing the dividing method'''
    if option_1[0]==1:
        train_data,train_target,test_data,test_target=random(feature,target)
    elif option_1[0]==2:
        train_data,train_target,test_data,test_target=self_determine(feature,target,option_2)
    elif option_1[0]==3:
        train_data,train_target,test_data,test_target=cross_val(feature,target,option_2)
    else:
        print("please fill with valid option")
        return None,None,None,None
    return train_data,train_target,test_data,test_target