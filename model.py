
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Questions(db.Model): 

	__tablename__ = "questions"

	question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	strand_id = db.Column(db.Integer)
	strand_name = db.Column(db.String)
	standard_id = db.Column(db.Integer)
	standard_name = db.Column(db.String)
	difficulty = db.Column(db.Float)

class Usage(db.Model): 

	__tablename__ = "usage"

	usage_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	student_id = db.Column(db.Integer)
	question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
	assigned_hours_ago = db.Column(db.Integer)
	answered_hours_ago = db.Column(db.Integer, nullable=True)

	question = db.relationship("Questions",

						   backref=db.backref("question_usage", order_by=question_id))



def connect_to_db(app):
	"""Connect the database to our Flask app."""

	# Configure to use our SQLite database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nri.db'
	db.app = app
	db.init_app(app)


if __name__ == "__main__":
	# As a convenience, if we run this module interactively, it will leave
	# you in a state of being able to work with the database directly.

	from server import app
	connect_to_db(app)
	print "Connected to DB."