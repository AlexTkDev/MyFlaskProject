from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def index():
    articles = Article.query.order_by(Article.date_posted.desc()).all()
    return render_template('index.html', articles=articles)


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date_posted.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:post_id>')
def posts_detail(post_id):
    article = Article.query.get(post_id)
    return render_template('post_detail.html', article=article)


@app.route('/posts/<int:post_id>/delete')
def posts_delete(post_id):
    article = Article.query.get_or_404(post_id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except Exception as e:
        return f"Failed to create article: {e}"


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        author = request.form['author']

        article = Article(title=title, intro=intro, text=text, author=author)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except Exception as e:
            return f"Failed to create article: {e}"
    else:
        return render_template('create.html')


@app.route('/posts/<int:post_id>/update', methods=['GET', 'POST'])
def post_update(post_id):
    article = Article.query.get(post_id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']
        article.author = request.form['author']

        try:
            db.session.commit()
            return redirect('/posts')
        except Exception as e:
            return f"При редактировании статьи произошла ошибка -> : {e}"
    else:
        return render_template('post_update.html', article=article)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=False)
