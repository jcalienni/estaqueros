from cmath import pi
from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def home():    
    return render_template('index.html')

@app.route("/calcular", methods=['POST'])
def calcular():
    test = int(request.form['cantidad'])
    return render_template('personas.html', cantidad = test, indice = 0)

if __name__ == "__main__":
    app.run()