from model import Questions, Usage, connect_to_db, db
from server import app

def load_questions(): 
	for i, row in enumerate(open("questions.csv")):
		row = row.rstrip()
		strand_id, strand_name, standard_id, standard_name, question_id, difficulty = row.split(",")
		print "this is the stuff",  strand_id, standard_name
		strand_id= int(strand_id)
		question_id=int(question_id)
		standard_id=int(standard_id)
		difficulty=float(difficulty)
		question = Questions(question_id=question_id,
				strand_id=strand_id, strand_name=strand_name, standard_id=standard_id, standard_name=standard_name, difficulty=difficulty)

		db.session.add(question)

	db.session.commit()

def load_usage():

	for i, row in enumerate(open("usage.csv")):
		row = row.rstrip()
		row = row.split(",")
		print "this is the row: ", row
		print len(row)
		usage_id, student_id, question_id, assigned_hours_ago, answered_hours_ago= row
		# student_id=int(student_id)
		# usage_id=int(usage_id)
		# question_id=int(question_id)
		# assigned_hours_ago=int(assigned_hours_ago)
		# answered_hours_ago=int(answered_hours_ago)
		usage = Usage(student_id=student_id, question_id=question_id, assigned_hours_ago=assigned_hours_ago, answered_hours_ago=answered_hours_ago)
		db.session.add(usage)
	db.session.commit()


if __name__ == "__main__":
	connect_to_db(app)
	db.create_all()

	load_questions()
	load_usage()
