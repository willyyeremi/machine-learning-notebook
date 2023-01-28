def multi_decision_tree(train_data,test_data,train_target,test_target,min_leaf,max_leaf):
    '''multi decision tree with different leaf node and find one with lowest MAE'''
    import pandas
    import sklearn.tree
    import sklearn.metrics
    # creating function to put into a loop
    def model(leaf_nodes,train_data,train_target,test_data,test_target):
        #syntax for choosing ML model
        decision_tree=sklearn.tree.DecisionTreeRegressor(max_leaf_nodes=leaf_nodes,random_state=1) 
        # syntax to train model
        decision_tree.fit(train_data,train_target) 
        #syntax to predict and store the prediction for accuracy check later
        prediction_decision_tree=decision_tree.predict(test_data) 
        # accuracy check with MAE
        MAE_value=sklearn.metrics.mean_absolute_error(test_target,prediction_decision_tree) 
        return(MAE_value)
    # creating a loop for finding minimum error from a range of leaf node
    list_MAE=[]
    for f in range (min_leaf,max_leaf):
        list_MAE.append(model(f,train_data,train_target,test_data,test_target))
    # creating table with MAE value and respective leaf nodes
    MAE_table=pandas.DataFrame(data={'MAE value':list_MAE,'Leaf':list(range(min_leaf,max_leaf))})
    # choosing the best MAE and leaf nodes
    decision_tree_MAE=min(MAE_table['MAE value'])
    optimum_leaf=MAE_table.loc[MAE_table[MAE_table['MAE value']==min(MAE_table['MAE value'])].index.to_numpy()[0],'Leaf']
    return decision_tree_MAE