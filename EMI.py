from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_emi(principal, rate, time):
    # EMI calculation logic (same as before)
    rate = rate / 12 / 100
    emi = (principal * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)
    return round(emi, 2)

@app.route('/', methods=['GET', 'POST'])
def emi_calculator():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        rate = float(request.form['rate'])
        time = int(request.form['time'])

        emi = calculate_emi(principal, rate, time)
        return render_template('result.html', emi=emi)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
