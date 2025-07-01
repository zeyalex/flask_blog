from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {'title': 'Перший пост', 'content': 'Це зміст першого поста.'},
    {'title': 'Другий пост', 'content': 'Ще трохи тексту для другого поста.'},
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
