import pickle

class Predict:

    def __init__(self):
        self.prediction_class = "Processing..."


    def get_model_file(self):
        location = 'Model_File/Model.pickle'
        return pickle.load(open(location,'rb'))

    def one_hot_encoding(self,value):
        try:
            if value == 2:
                return [1.0,0.0,0.0,0.0,0.0]
            elif value == 3:
                return [0.0,1.0,0.0,0.0,0.0,0.0]
            elif value == 4:
                return [0.0,0.0,1.0,0.0,0.0]
            elif value == 5:
                return [0.0,0.0,0.0,1.0,0.0]
            elif value == 6:
                return [0.0,0.0,0.0,0.0,1.0]

            else:
                return "Invalid Input"
        except Exception as e:
            print("Error in on_hot_encoding:",e)
    # rate_marriage	age	yrs_married	children	religious	educ	occupation	occupation_husb

    def get_result_from_model(self,model_,v1,v2,v3,v4,v5,v6,v7,v8):
        try:
            other_feature = [v1,v2,v3,v4,v5,v6]
            encode_value_1 = self.one_hot_encoding(v7)
            encode_value_2 = self.one_hot_encoding(v8)
            """
            print(f'v1:{v1}', type(v1))
            print(f'v2:{v2}', type(v2))
            print(f'v3:{v3}', type(v3))
            print(f'v4:{v4}', type(v4))
            print(f'v5:{v5}', type(v5))
            print(f'v6:{v6}', type(v6))
            print(f'v7:{v7}', type(v7))
            print(f'v8:{v8}', type(v8))
            """
            value_list = [1] + encode_value_1 + encode_value_2 + other_feature
            predicted_value = model_.predict([value_list])
            return predicted_value
        except Exception as e:
            print("Error in get_result:",e)

    def main(self,rate_marriage,age,yrs_married,child,reli,educ,o_w,o_husb):
        try:
            model_file = self.get_model_file()
            prediction_result = self.get_result_from_model(model_file,float(rate_marriage),float(age),float(yrs_married)
                                                           ,float(child),float(reli),float(educ),float(o_w),float(o_husb))
            #print(prediction_result[0])
            if prediction_result[0] == 0.0 or prediction_result[0] < 0.0:
                self.prediction_class = 'No Chance of Affair'
            elif prediction_result[0] > 0.0:
                self.prediction_class = 'Chances Of Affair'
            else:
                self.prediction_class = 'Error'
            # return self.prediction_result
           # print("self.prediction_class:",self.prediction_class)
        except Exception as e:
            print("Error in main of predict class:", e)

    def result(self):
        #print(self.prediction_class)
        return self.prediction_class


"""if __name__ =='__main__':
    obj = Predict()
    obj.main(5,56,4,1,1,12,6,2)
    print(obj.result())
    
    """
    
