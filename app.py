from flask import Flask, render_template
import os

app = Flask(__name__)

posts = [
    {'title': 'Перший пост', 'content': 'Це зміст першого поста.'},
    {'title': 'Другий пост', 'content': 'Ще трохи тексту для другого поста.'},
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
