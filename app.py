from flask import Flask, jsonify, request, render_template
import google.generativeai as genai

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
        return "Your Question: " + " " + request.form['userquery']


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


if __name__ == '__main__':
    app.run(port=5000, debug=True)
