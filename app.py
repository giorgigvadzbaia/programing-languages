from flask import Flask, render_template

app = Flask(__name__)

@app.route('/programing-languages')
def lang():
    data = [
        {'name': 'python', 'description': 'blabla', 'link': 'https://www.python.org/'},
        {'name': 'c++', 'description': 'blabla', 'link': 'https://en.wikipedia.org/wiki/C%2B%2B'},
        {'name': 'java', 'description': 'blabla', 'link': 'https://en.wikipedia.org/wiki/Java_%28programming_language%29'},
        {'name': 'javascript', 'description': 'blabla', 'link': 'https://en.wikipedia.org/wiki/Java_%28programming_language%29'},
        {'name': 'typescript', 'description': 'blabla', 'link': 'https://en.wikipedia.org/wiki/TypeScript/'}

    ]
    python = data[0]['name']
    return render_template('index.html', data=data)


if __name__ = '__main__'
    app.run(debug=True)
