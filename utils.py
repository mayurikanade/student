import pickle
import json
import numpy as np
import config


class StudentPerformance():
    def __init__(self,hours_studied,previous_scores,extracurricular_activities,sleep_hours,
                 sample_question_papers_practiced):
        print("****** INIT Function *********")
        self.hours_studied = hours_studied
        self.previous_scores= previous_scores
        self.extracurricular_activities = extracurricular_activities
        self.sleep_hours = sleep_hours
        self.sample_question_papers_practiced = sample_question_papers_practiced
        

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):
        self.__load_saved_data()

        
        extracurricular_activities =self.json_data['Extracurricular_Activities'][self.extracurricular_activities]


        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.hours_studied
        test_array[0,1] = self.previous_scores
        test_array[0,2] = extracurricular_activities
        test_array[0,3] = self.sleep_hours
        test_array[0,4] = self.sample_question_papers_practiced


        predicted_charges = np.around(self.model.predict(test_array)[0],3)
        
        return predicted_charges


