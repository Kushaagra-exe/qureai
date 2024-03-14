from flask import Flask, jsonify, request, render_template
import google.generativeai as genai
from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np
from tensorflow.keras.models import load_model


def predict(values, dic):
    if len(values) == 8:
        model = pickle.load(open('models/diabetes.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 26:
        model = pickle.load(open('models/breast_cancer.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 13:
        model = pickle.load(open('models/heart.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 18:
        model = pickle.load(open('models/kidney.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 10:
        model = pickle.load(open('models/liver.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]


app = Flask(__name__)
genai.configure(api_key="AIzaSyDl9IMiuDS254NMT3l02pYOuOw0UUz0IFk")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompts = [
    "I'm working on a fictional scenario for a patient experiencing {}. The patient is a {}-year-old {} with",
    "a history of {}",
    "They recently traveled to {} ",
    "and might have been exposed to {}",
    "Can you provide a list of possible diseases that could cause these symptoms? It's important to emphasize that this is for informational purposes only and consulting a doctor is crucial for proper diagnosis and treatment.",
    "Please only provide the list of possible diseases and information in a list form about them nothing else "

]



# prompt = .format(symptoms, age, gender, med_history, tavel_history, exposture)


# def gemini():


@app.route('/')
def work():
    return "Working"


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('tempform.html')
    if request.method == 'POST':
        data = request.form
        return jsonify(data)


# @app.route('/chatbot', methods=['GET', 'POST'])
# def chatbot():

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'GET':
        return render_template('ai.html')
    if request.method == 'POST':
        jsonresp = ["input:{}".format(request.form),
                    "output: ",
                    ]

        response = model.generate_content(jsonresp)
        # resp = {'resp':response}
        rresp = "Your Question: " + " " + request.form['userquery'] + " <br> " + str(response.text)
        return rresp, 200




@app.route('/submit-data', methods=['GET', 'POST'])
def submit_data():
    if request.method == 'POST':
        data = request.form
        symptoms = data['symptoms']
        age = data['age']
        gender = data['gender']
        med_history = data['med_history']
        tavel_history = data['tavel_history']
        exposture = data['exposture']
        final_prompt = prompts[0].format(symptoms, age, gender)
        if (med_history):
            final_prompt = final_prompt + prompts[1].format(med_history)
        else:
            final_prompt = final_prompt + "no medical history"

        if (tavel_history):
            final_prompt = final_prompt + prompts[2].format(tavel_history)
        else:
            final_prompt = final_prompt + "NO recent travelling"

        if (exposture):
            final_prompt = final_prompt + prompts[3].format(exposture)

        final_prompt = final_prompt + prompts[4] + prompts[5]

        jsonresp = ["input:{}".format(final_prompt),
                    "output: ",
        ]

        response = model.generate_content(jsonresp)
        # resp = {'resp':response}
        return str(response.text), 200

    elif request.method == 'GET':
        return render_template('tempform.html')


@app.route('/submit-test', methods=['POST'])
def submit_test():
    data = request
    return data


@app.route("/diabetes", methods=['GET', 'POST'])
def diabetesPage():
    to_predict_dict = request.form.to_dict()
    to_predict_list = list(map(float, list(to_predict_dict.values())))
    pred = predict(to_predict_list, to_predict_dict)
    return pred

@app.route("/cancer", methods=['GET', 'POST'])
def cancerPage():
    to_predict_dict = request.form.to_dict()
    to_predict_list = list(map(float, list(to_predict_dict.values())))
    pred = predict(to_predict_list, to_predict_dict)
    return pred

@app.route("/heart", methods=['POST'])
def heartPage():
    to_predict_dict = request.form.to_dict()
    to_predict_list = list(map(float, list(to_predict_dict.values())))
    pred = predict(to_predict_list, to_predict_dict)
    return pred

@app.route("/kidney", methods=['POST'])
def kidneyPage():
    to_predict_dict = request.form.to_dict()
    to_predict_list = list(map(float, list(to_predict_dict.values())))
    pred = predict(to_predict_list, to_predict_dict)
    return pred

@app.route("/liver", methods=['POST'])
def liverPage():
    to_predict_dict = request.form.to_dict()
    to_predict_list = list(map(float, list(to_predict_dict.values())))
    pred = predict(to_predict_list, to_predict_dict)
    return pred

@app.route("/malaria", methods=['POST'])
def malariaPage():
    to_predict_dict = request.form.to_dict()
    to_predict_list = list(map(float, list(to_predict_dict.values())))
    pred = predict(to_predict_list, to_predict_dict)
    return pred

@app.route("/pneumonia", methods=['POST'])
def pneumoniaPage():
    to_predict_dict = request.form.to_dict()
    to_predict_list = list(map(float, list(to_predict_dict.values())))
    pred = predict(to_predict_list, to_predict_dict)
    return pred


if __name__ == '__main__':
    app.run(port=5000, debug=True)
