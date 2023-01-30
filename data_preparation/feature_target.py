def numerical_feature(data,feature):
    '''for selecting feature from column with numeric data'''
    import pandas
    # feature checking 
    not_exist=[]
    wrong_type=[]
    for i in feature:
        if i not in data.columns:
            not_exist.append(i)
        if i not in not_exist:
            if data[i].dtypes not in ["int64","float64"]:
                wrong_type.append(i)
    if len(not_exist)!=0:
        print("columns name inside the list below doesn't exist. please input valid column name")
        print(not_exist)
    if len(wrong_type)!=0:
        print("columns name inside the list below have wrong data type. please input valid column name")
        print(wrong_type)  
    # validation if feature is valid or not
    if len(not_exist)!=0 or len(wrong_type)!=0:
        numerical_feature(data)
    else:
        return feature

def ordinal_feature(data,feature):
    '''for for selecting feature from column with categorical data with ordinality'''
    import pandas
    # determining for the need of this function
    question=input("do you want to include column with categorical data and have ordinality?\ny: Yes\nn: No\n")
    if question.upper not in ["Y","N"]:
        print("enter valid answer")
        ordinal_feature()
    elif question.upper=="y":
        # feature checking 
        not_exist=[]
        wrong_type=[]
        for i in feature:
            if i not in data.columns:
                not_exist.append(i)
            if data[data[i]].dtypes!="object":
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