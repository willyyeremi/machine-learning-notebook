def categorical_handle(train_data,test_data,list_column_OE,list_column_OHE):
    '''handling categorical data with ordinal, one-hot, and target encoding'''
    import pandas
    import sklearn.preprocessing
    #Ordinal Encoding
    if len(list_column_OE)!=0:
        # change the value of column with object data type with ordinal encode function
        train_data[list_column_OE] = sklearn.preprocessing.OrdinalEncoder().fit_transform(train_data[list_column_OE]) 
        test_data[list_column_OE] = sklearn.preprocessing.OrdinalEncoder().transform(test_data[list_column_OE])
    # One Hot Encoding
    if len(list_column_OHE)!=0:
        # load the one hot encode function
        OH_encoder=sklearn.preprocessing.OneHotEncoder(handle_unknown='ignore',sparse=False) 
        # creating dataframe from categorical column with unique value per column as new colum name
        OH_column_train=pandas.DataFrame(OH_encoder.fit_transform(train_data[list_column_OHE])) 
        OH_column_test=pandas.DataFrame(OH_encoder.transform(test_data[list_column_OHE]))
        # put index to new created dataframe because one hot encoding remove index
        OH_column_train.index=train_data.index 
        OH_column_test.index=test_data.index
        # drop original column from dataframe
        train_data=train_data.drop(list_column_OHE,axis=1)
        test_data=test_data.drop(list_column_OHE,axis=1)
        # combine the new column to the original data
        train_data=pandas.concat([train_data,OH_column_train], axis=1) 
        test_data=pandas.concat([test_data,OH_column_test], axis=1)
    # Target Encoding