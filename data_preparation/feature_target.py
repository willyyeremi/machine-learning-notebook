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
        return []
    elif len(feature)<1:
        print("numerical feature must not empty. please select numerical feature.")
    else:
        return feature

def categorical_feature(data,feature):
    '''for for selecting feature from column with categorical data with ordinality'''
    import pandas
    if len(feature)!=0:
        # feature checking 
        not_exist=[]
        wrong_type=[]
        for i in feature:
            if i not in data.columns:
                not_exist.append(i)
            if i not in not_exist:    
                if data[i].dtypes!="object":
                    wrong_type.append(i)
        if len(not_exist)!=0:
            print("columns name inside the list below doesn't exist. please input valid column name")
            print(not_exist)
        if len(wrong_type)!=0:
            print("columns name inside the list below have wrong data type. please input valid column name")
            print(wrong_type)  
        # validation if feature is valid or not
        if len(not_exist)!=0 or len(wrong_type)!=0:
            return []
        else:
            return feature

def categorical_check(data,ordinal_feature,oh_feature,target_feature):
    wrong=[]
    ordinal_oh=[]
    ordinal_target=[]
    oh_target=[]
    for i in ordinal_feature:
        for j in oh_feature:
            if i==j:
                ordinal_oh.append(j)
                wrong.append(j)
        for k in target_feature:
            if i==k:
                ordinal_target.append(k)
                wrong.append(k)
    for j in oh_feature:
        for k in target_feature:
            if j==k:
                oh_target.append(k)
                wrong.append(k)
    if len(wrong)!=0:
        print("the listed feature placed at ordinal_feature and oh_feature. please remove from one of the list.")
        print(ordinal_oh)
        print("the listed feature placed at ordinal_feature and target_feature. please remove from one of the list.")
        print(ordinal_target)
        print("the listed feature placed at target_feature and oh_feature. please remove from one of the list.")
        print(oh_target)
        return []
    else:
        categorical=[]
        if len(ordinal_feature)>0:
            categorical.append(categorical_feature(data,ordinal_feature))
        if len(ordinal_feature)>0:    
            categorical.append(categorical_feature(data,oh_feature))
        if len(ordinal_feature)>0:
            categorical.append(categorical_feature(data,target_feature))
        return categorical
