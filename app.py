from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/more')
def more():
    return render_template('more.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ppage', methods=['GET', 'POST'])
def ppage():
    return render_template('programPage.html')

@app.route('/upper', methods=['GET', 'POST'])
def upper():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('toUpper.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            if radius >=0:
                area = 3.14159 * radius**2
                result = f"The area of the circle with the radius of {radius} is {area: .2f}"
            else:
                result = "Radius should be a non-negative number."
        except ValueError:
            result = "Invalid input. Please enter a valid number for radius."

    return render_template('circle.html', result=result)


@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            if base >=0 and height >= 0:
                area = 0.5 * base * height
                result = f"The area of the triangle with a base of {base} and height of {height} is {area:.2f} square units."
            else:
                result = "Base and height should be a non-negative number."
        except ValueError:
            result = "Invalid input. Please enter a valid number for base and height."

    return render_template('triangle.html', result=result)



@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
