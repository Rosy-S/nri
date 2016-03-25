from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, jsonify, flash
from model import Questions, Usage, connect_to_db, db, get_count
from random import randrange
app = Flask(__name__)
app.secret_key = "someFancySecret"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def get_question():
	resp = request.form["question_amount"]
	print 'This is the amount of quesitons: ',resp
	resp = int(resp)
	if resp < 0: 
		flash("Invalid amount of quesitons. Must be above 0")
		return redirect("/")
	amount_of_questions = db.session.query(Questions).count()
	if resp > amount_of_questions:
		flash("Not enough questions for that number, please pick a number up to " + str(amount_of_questions))
		return redirect("/")
	else: 
		strand_1_questions = Questions.query.filter(Questions.strand_id == 1).all()
		strand_1_questions_amount = len(strand_1_questions)
		strand_2_questions = Questions.query.filter(Questions.strand_id == 2).all()
		strand_2_questions_amount = len(strand_2_questions)
		results = []
		while resp > 0:
			results.append(strand_1_questions[randrange(0,strand_1_questions_amount)].question_id)
			resp -=1
			if resp ==0: 
				break
			results.append(strand_2_questions[randrange(0,strand_2_questions_amount)].question_id)
			resp -=1
		# Tim sort algorithm in Python is optimized to be the fastest than any native algorigthm we can implement

		results.sort()



	return render_template("results.html", results=results)



if __name__ == "__main__":

	app.debug = True

	connect_to_db(app)

	app.run()