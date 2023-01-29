def numerical_feature(data):
    '''for selecting feature from column with numeric data'''
    import pandas
    # selecting feature
    feature=list(map(str,input("write columns name with numeric data that will be used as feature separeted with comma\n").split(",")))
    # feature checking 
    not_exist=[]
    wrong_type=[]
    for i in feature:
        if i not in feature:
            not_exist.append(i)
        if data[data[i]].dtypes!=int or data[data[i]].dtypes!=float:
            wrong_type.append(i)
    if len(not_exist)!=0:
        print("columns name inside the list below doesn't exist. please input valid column name")
        print(not_exist)
    if len(wrong_type)!=0:
        print("columns name inside the list below have wrong data type. please input valid column name")
        print(wrong_type)  
    # validation if feature is valid or not
    if len(not_exist)!=0 or len(wrong_type)!=0:
        numerical_feature()
    else:
        return feature

def ordinal_feature():
    '''for for selecting feature from column with categorical data with ordinality'''
    import pandas
    # determining for the need of this function
    question=input("do you want to include column with categorical data and have ordinality?\ny: Yes\nn: No\n")
    if question.upper not in ["Y","N"]:
        print("enter valid answer")
        ordinal_feature()
    elif question.upper=="y":
        # selecting feature
        feature=list(map(str,input("write columns name with categorical data that will be used as feature separeted with comma\n").split(",")))
        # feature checking 
        not_exist=[]
        wrong_type=[]
        for i in feature:
            if i not in feature:
                not_exist.append(i)
            if data[data[i]].dtypes!=object:
                wrong_type.append(i)
        if len(not_exist)!=0:
            print("columns name inside the list below doesn't exist. please input valid column name")
            print(not_exist)
        if len(wrong_type)!=0:
            print("columns name inside the list below have wrong data type. please input valid column name")
            print(wrong_type)  
        # validation if feature is valid or not
        if len(not_exist)!=0 or len(wrong_type)!=0:
            numerical_feature()
        else:
            return feature