def numerical_check(data,feature):
    '''for checking numerical feature input validity'''
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
        numerical_feature(data,feature)
    else:
        return feature

def categorical_valid(data,feature):
    '''for checking categorical feature input validity'''
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

def categorical_duplicate(oe_feature,ohe_feature,te_feature):
    '''for checking is there duplicate target on different category
    oe_feature: feature with ordinality
    ohe_feature: feature without ordinality and <=10 categories
    te_feature: feature without ordinality and >10 categories'''
    ordinal_oh=[]
    ordinal_target=[]
    oh_target=[]
    for i in oe_feature:
        for j in ohe_feature:
            if i==j:
                ordinal_oh.append(j)
        for k in te_feature:
            if i==k:
                ordinal_target.append(k)
    for j in ohe_feature:
        for k in te_feature:
            if j==k:
                oh_target.append(k)
    if len(ordinal_oh)!=0:
        print("the listed feature placed at ordinal_feature and oh_feature. please remove from one of the list.")
        print(ordinal_oh)
    if len(ordinal_target)!=0:
        print("the listed feature placed at ordinal_feature and target_feature. please remove from one of the list.")
        print(ordinal_target)
    if len(oh_target)!=0:
        print("the listed feature placed at target_feature and oh_feature. please remove from one of the list.")
        print(oh_target)
    if len(ordinal_oh)>0 or len(ordinal_target)>0 or len(oh_target)>0:
        return False
    else:
        return True

def categorical_check(data,oe_feature,ohe_feature,te_feature):
    '''for wrapping validity and duplicate check on categorical feature
    oe_feature: feature with ordinality
    ohe_feature: feature without ordinality and <=10 categories
    te_feature: feature without ordinality and >10 categories'''
    if categorical_duplicate(oe_feature,ohe_feature,te_feature)==False:
        categorical_check(data,oe_feature,ohe_feature,te_feature)
    else:
        categorical=[]
        if len(oe_feature)>0:
            categorical=categorical+categorical_valid(data,oe_feature)
        if len(ohe_feature)>0:    
            categorical=categorical+categorical_valid(data,ohe_feature)
        if len(te_feature)>0:
            categorical=categorical+categorical_valid(data,te_feature)
        return categorical
