from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import Callable


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Float: Callable


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = MySQLAlchemy(app)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         rep = "Person(" + self.name + "," + str(self.age) + ")"
#         return rep
#
#
# person = Person("John", 20)
# print(repr(person))
# print(person)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__} - <{self.title}>"


db.create_all()

# new_book = Book(title="ghi", author="789", rating=9.0)
# db.session.add(new_book)
# db.session.commit()
# print(repr(new_book))

all_books = db.session.query(Book).all()
print(all_books)
for x in all_books:
    print(x.title, x.author, x.rating)

# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)

# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()
# print(book_to_update)

# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()
# print(book_to_update)

# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
# print(book_to_delete)

