import pickle

class Predict:

    def get_model_file(self):
        location = 'Model_File/Model.pickle'
        return pickle.load(open(location,'rb'))

    def one_hot_encoding(self,value):
        try:
            if value == 1:
                return [1.0,0.0,0.0,0.0,0.0,0.0]
            elif value == 2:
                return [0.0,1,0.0,0.0,0.0,0.0]
            elif value == 3:
                return [0.0,0.0,1.0,0.0,0.0,0.0]
            elif value == 4:
                return [0.0,0.0,0.0,1.0,0.0,0.0]
            elif value == 5:
                return [0.0,0.0,0.0,0.0,1.0,0.0]
            elif value == 6:
                return [0.0,0.0,0.0,0.0,0.0,1.0]
            else:
                return "Invalid Input"
        except Exception as e:
            print("Error in on_hot_encoding:",e)
    # rate_marriage	age	yrs_married	children	religious	educ	occupation	occupation_husb

    def get_result(self,model_,v1,v2,v3,v4,v5,v6,v7,v8):

        other_feature = [v1,v2,v3,v4,v5,v6]
        encode_value_1 = self.one_hot_encoding(v7)
        encode_value_2 = self.one_hot_encoding(v8)
        value_list = [1] + encode_value_1 + encode_value_2 + other_feature
        predicted_value = model_.predict([value_list])
        return predicted_value

    def main(self,rate_marriage,age,yrs_married,child,reli,educ,o_w,o_husb):
        try:
            model_file = self.get_model_file()
            prediction_result = self.get_result(model_file,rate_marriage,age,yrs_married,child,reli,educ,o_w,o_husb)
            return prediction_result
        except Exception as e:
            print("Error in main of predict class:", e)