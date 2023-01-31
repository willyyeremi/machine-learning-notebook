def self_determine(feature,target,ratio):
    '''divide between train and test with ratio'''
    import pandas
    total_row=feature.shape[0]
    total_ratio=ratio[0]+ratio[1]
    train_data=feature[:(total_row//total_ratio*ratio[0])]
    train_target=target[:(total_row//total_ratio*ratio[0])]
    test_data=feature[(total_row//total_ratio*ratio[0]+1):]
    test_target=target[(total_row//total_ratio*ratio[0]+1):]
    return train_data,test_data,train_target,test_target

