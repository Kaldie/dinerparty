from server.app import db

class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jTokenId = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jTokenId):
        query = cls.query.filter_by(jTokenId = jTokenId).first()
        return bool(query)