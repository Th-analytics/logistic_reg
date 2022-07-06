from flask import Flask, render_template, request, redirect, url_for
from prediction import Predict
import threading
from math import floor

app = Flask(__name__)
global free_status, result_data
free_status = True
result_data = 'Processing'


class Threading:

    def __init__(self, object, rate_m, age, yrs_marr, child_, reli_, educ_, oc_w, oc_husb):
        self.object = object
        self.rate_m = rate_m
        self.age = age
        self.yrs_marr = yrs_marr
        self.child_ = child_
        self.reli_ = reli_
        self.educ_ = educ_
        self.oc_w = oc_w
        self.oc_husb = oc_husb
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        global free_status
        free_status = False
        threading.Thread(target=self.object.main()).start()
        free_status = True


@app.route('/', methods=['POST', 'GET'])
def home():
    global free_status

    if request.method == 'POST':
        if free_status != True:
            return "Website is Busy"
        else:
            free_status = True
        # Default Values

        age = request.form['age']  # Age of Women
        marr_rating = request.form['rate_m']  # marriage rating
        education = request.form['edu_scale']
        yrr_married = request.form['yom']
        religious = request.form['R_scale']
        occ_women = request.form['occ_w']
        occ_men = request.form['occ_m']
        children = request.form['children']
        print("Marriage:", marr_rating)
        print("age: ", age)
        print("Education:", education)
        print("Years Married: ",yrr_married)
        print("religious: ", religious)
        print("Occ_women:", occ_women)
        print("Occ_men:", occ_men)
        print("Children:", children)

        #Threading(object=object_pre, values=data_values)
        return redirect(url_for('result'))
    else:
        return render_template('index.html')


@app.route('/result', methods=['GET'])
def result():
    global result_data
    if result_data != 'Processing...':
        result_data = 0
    print("result_data: ", result_data)
    return render_template('result.html', re_data=result_data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
    object_pre = Predict()
