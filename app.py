from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Концфігурація бази даних (SQLite)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# модель Post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Головна сторінка з постами
@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

# Створення нового поста
@app.route('/create', methods=['GET', 'POST'])
def create():
        if request.method == 'POST':
             title = request.form['title']
             content = request.form['content']
             new_post = Post(title=title, content=content)
             db.session.add(new_post)
             db.session.commit()
             return redirect(url_for('home'))
        return render_template('create.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    with app.app_context():
        db.create_all()  # створює таблиці при першому запуску
    app.run(host='0.0.0.0', port=port, debug=True)
