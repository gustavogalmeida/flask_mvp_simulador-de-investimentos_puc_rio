from app import db

class Simulacao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(30), nullable=False)
    valor_aplicado = db.Column(db.Float, nullable=False)
    cdi = db.Column(db.Float, nullable=False)
    cdi_sobras = db.Column(db.Float, nullable=False)
    dias = db.Column(db.Integer, nullable=False)
    rentabilidade_bruta = db.Column(db.Integer, nullable=False)
    saldo_total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name