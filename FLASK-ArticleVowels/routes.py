from flask import Flask 
from flask import render_template, request

app = Flask(__name__)

def checkVowels(word):
    vowelsUpper = ('A','E', 'I', 'O', 'U')
    vowelsLower = ('a', 'e', 'i', 'o', 'u')
    article = ''
    if word.startswith(vowelsUpper) or word.startswith(vowelsLower):
        article = 'an'
    else:
        article = 'a'
    return article

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/output',methods=['GET', 'POST'])
def output():
    formData = request.form.get('article')
    formData = str(formData)
    article = checkVowels(formData)
    return render_template('output.html', article = article, formData=formData )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6500, debug=True)
