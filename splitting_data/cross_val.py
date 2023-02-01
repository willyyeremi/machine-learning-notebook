def cross_val(feature,target,fold):
    '''cross validation method'''
    import pandas
    if len(fold)!=1:
       print("the ratio filling of ratio variable is not following the format. please check again.")
    elif type(fold[0])!="int64":
        print("please fill the variable_split only with int type data")
    elif fold<5:
        print('the minimum input of variable split for this method is 5. please correct it')
    else:
