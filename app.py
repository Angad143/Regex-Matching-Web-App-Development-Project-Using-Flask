from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['testString']
    regex_pattern = request.form['regexPattern']
    matches = []
    try:
        import re
        regex = re.compile(regex_pattern)
        matches = regex.findall(test_string)
    except re.error:
        pass  # Handle invalid regex pattern
    return render_template('results.html', matches=matches)

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = validate_email_address(email)
    return render_template('email_validation.html', is_valid=is_valid, email=email)

def validate_email_address(email):
    import re
    # Regular expression for basic email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

if __name__ == '__main__':
    app.run(debug=True)
