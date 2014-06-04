#class Post:
#	def __init__(self,title, author, content):
#		self.title = title
#		self.author = author
#		self.content = content


from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(120))
	lastname = db.Column(db.String(120))
	username = db.Column(db.String(120), unique = True)
	posts = db.relationship('Post', backref = 'author')

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(120))
	content = db.Column(db.Text)
	author_id = db.Column(db.Integer, db.ForeignKey ('user.id'))

		

