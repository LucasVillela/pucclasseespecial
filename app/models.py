from app import db



class Aluno(db.Model):
	ra = db.Column(db.String(20), primary_key=True)
	nome = db.Column(db.String(120))
	sobrenome = db.Column(db.Date)
	senha = db.Column(db.String(50))
	cod_curso = db.Column(db.Integer)

	def __repr__(self):
		return '<Client %r>' % (self.nickname)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.ra)  # python 2
		except NameError:
			return str(self.ra)  # python 3
