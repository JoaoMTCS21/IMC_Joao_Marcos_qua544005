from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    massa = None
    altura = None
    diagnostico = None
    result = None

    if request.method == "POST":
        massa = float(request.form.get("massa", "").replace(',', '.'))
        altura = float(request.form.get("altura", "").replace(',', '.'))
        imc = massa / (altura ** 2)
        result = round(imc, 2)

        if imc < 18.5:
            diagnostico = "Abaixo do peso"
        elif imc < 25:
            diagnostico = "Peso normal"
        elif imc < 30:
            diagnostico = "Sobrepeso"
        elif imc < 35:
            diagnostico = "Obesidade grau I"
        elif imc < 40:
            diagnostico = "Obesidade grau II"
        else:
            diagnostico = "Obesidade grau III"
        result = f'Seu IMC é {imc:.2f}.\n{diagnostico}'
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)