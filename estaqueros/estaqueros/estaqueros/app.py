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

@app.route("/resumen", methods=['POST'])
def resumen():
    personas = []
    montos = []
    cantidad = int(len(request.form)/2)
    for persona in range(1, (cantidad+1)):
        personas.append(request.form["p"+str(persona)])
        montos.append(request.form["c"+str(persona)])
    return render_template('resumen.html', personas = personas, montos = montos)

if __name__ == "__main__":
    app.run()