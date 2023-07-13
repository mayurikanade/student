from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import StudentPerformance
import config
import traceback
app = Flask(__name__)

@app.route('/student')
def home1():
    
    return render_template('student.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    try:
        if request.method == 'GET':
            print("+"*50)
            data = request.args.get
            print("Data :",data)
            hours_studied = int(data('hour_studied'))
            previous_scores = int(data('previous_scores'))
            extracurricular_activities = data('extracurricular_activities')
            sleep_hours = int(data('sleep_hours'))
            sample_question_papers_practiced =int(data('sample_question_papers_practiced'))
            

            Obj= StudentPerformance(hours_studied,previous_scores,extracurricular_activities,
                                   sleep_hours,sample_question_papers_practiced)
            pred_price = Obj.get_predicted_price()
            
            # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
            return render_template('student.html', prediction = pred_price)

        elif request.method == 'POST':
            print("*"*40)
            data = request.form.get
            print("Data :",data)
            hours_studied = int(data('hours_studied'))
            previous_scores = int(data('previous_scores'))
            extracurricular_activities = data('extracurricular_activities')
            sleep_hours = int(data('sleep_hours'))
            sample_question_papers_practiced = int(data('sample_question_papers_practiced'))
           

            Obj =StudentPerformance(hours_studied,previous_scores,extracurricular_activities,
                                    sleep_hours,sample_question_papers_practiced)
            pred_price = Obj.get_predicted_price()
            
            # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
            return render_template('student.html', prediction = pred_price)

    except:
        print(traceback.print_exc())
        return redirect(url_for('student'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
