from flask import Flask, request, render_template, redirect , url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


# ========== Setup App & DB =========

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


# ============ SQLAlchemy ===========

class Book(db.Model):
    bookId = db.Column(db.Integer, primary_key=True)
    bookTitle = db.Column(db.String(50), nullable=False)
    bookAuthor = db.Column(db.String(50), nullable=False)
    bookYear = db.Column(db.Integer)

    def __init__(self, bookTitle, bookAuthor, bookYear):
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.bookYear = bookYear



# =========== Flask ============
@app.route("/")
@app.route("/book", methods=['POST','GET'])
def book():
    if request.method == 'POST':
        bTitle = request.form['bookTitle']
        bAuthor = request.form['bookAuthor']
        bYear = int(request.form['bookYear'])

        new_book = Book(bTitle, bAuthor, bYear)
        db.session.add(new_book)
        db.session.commit()

        flash("Book Added Successfully...")
        return redirect(url_for("books")) 
    else:
       return render_template("create_book.html") 


@app.route("/update/<int:book_id>", methods=['POST','GET'])
def update(book_id):

    found_book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        nTitle = request.form['newTitle']
        nAuthor = request.form['newAuthor']
        nYear = int(request.form['newYear'])

        found_book.bookTitle = nTitle
        found_book.bookAuthor = nAuthor
        found_book.bookYear = nYear

        db.session.commit()

        flash("Updated Successfully...")
        return redirect(url_for("books"))
    else:
        return render_template("update_book.html", book=found_book)


@app.route("/get_book/<int:book_id>", methods=['GET'])
def get_book(book_id):
    found_book = Book.query.get_or_404(book_id)
    return render_template("book_info.html", book=found_book)


@app.route("/books", methods=['GET'])
def books():
    all_books = Book.query.all()
    return render_template("books.html", books=all_books)


@app.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    book_to_delete = Book.query.get_or_404(book_id)

    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for("books"))


if __name__ == "__main__":
    app.run(debug=True)