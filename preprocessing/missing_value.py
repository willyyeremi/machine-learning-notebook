def missing_value(train_data,test_data,numerical_feature):
    '''replace missing value with mean and give extra information in new columnn wether the value is missing or not in binary value'''
    import pandas
    import sklearn.impute
    # list of column with missing value from train set
    columns_missing_value=[] 
    for col in list(train_data[numerical_feature].columns):
        if train_data[col].isnull().values.any()==True:
            columns_missing_value.append(col)
    # create new column with boolean value to indicate is the value of column missing or not
    for col in columns_missing_value: 
        train_data[col+'_is_missing']=train_data[col].isnull().astype(int)
        test_data[col+'_is_missing']=test_data[col].isnull().astype(int)    
    # create new dataframe with imputed value.
    train_data_imputed=pandas.DataFrame(sklearn.impute.SimpleImputer().fit_transform(train_data[columns_missing_value])) 
    test_data_imputed=pandas.DataFrame(sklearn.impute.SimpleImputer().fit_transform(test_data[columns_missing_value]))
    # imputation remove column name and index. put it back with column name from original data.
    train_data_imputed.columns=train_data[columns_missing_value].columns 
    test_data_imputed.columns=test_data[columns_missing_value].columns
    # make the imputed data as main data.
    for col in columns_missing_value: 
        train_data[col]=train_data_imputed[col].values
        test_data[col]=test_data_imputed[col].values
