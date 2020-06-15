from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/viewer')
def viewer():
    return render_template('viewer.html')

@app.route('/faq')
def faq():
    with open('./data/faq.json', encoding="utf8") as faq_json:
        faq = json.load(faq_json)
        return render_template('faq.html', faq=faq)
    






if __name__ == '__main__':
    app.run(debug=True)
