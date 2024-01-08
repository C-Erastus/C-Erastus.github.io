from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/academy')
def academy():
    return render_template('academy.html')

# The Blog goes here

@app.route('/travels')
def travels():
    return render_template('travels.html')

@app.route('/arts')
def arts():
    return render_template('arts.html')

@app.route('/sports')
def sports():
    return render_template('sports.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
