from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app import db

class Secret(db.Model):
    __tablename__ = 'secrets'
    id = db.Column(db.Integer,primary_key=True)
    
    secret_phrase = db.Column(db.String,nullable=True)
    secret_text = db.Column(db.String,nullable=False)
    secret_key = db.Column(String(36),  nullable=False,name='secret_key')

    def __repr__(self):
        return f'<User - {self.secret_name}'
    
    def get_id(self):
        return self.id