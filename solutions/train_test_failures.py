print(pd.DataFrame({"train": y_train.apply(sum, axis = 0), "test": y_test.apply(sum, axis = 0)}))