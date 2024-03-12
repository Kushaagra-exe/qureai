from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


@app.route('/')
def work():
    return "Working"

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template('tempform.html')
    if request.method=='POST':
        data = request.form
        return jsonify(data)


@app.route('/submit-data', methods=['POST'])
def submit_data():
    data = request.form
    print("Received data:", data)
    return jsonify(data), 200


if __name__=='__main__':
    app.run(port=5000, debug=True)