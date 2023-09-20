from app import db, login
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash
    

class User(UserMixin, db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64), index=True)
    last_name=db.Column(db.String(64), index=True)
    username=db.Column(db.String(64), index=True, unique=True)
    email=db.Column(db.String(64), index=True, unique=True)
    phone=db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    user_plants= db.relationship('Plant', backref='grower', lazy='dynamic')
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f'<User {self.username}>'
    


class Plant(UserMixin, db.Model):
    id=db.Column(db.Integer,primary_key=True)
    plant_name=db.Column(db.String(64), index=True)
    #plant_photo=#TODO  # ovo moram skontati kako naknadno da dodam
    plant_moisture=db.Column(db.Integer)
    plant_sunlight=db.Column(db.String(140))
    plant_outside_temp=db.Column(db.String(140))
    plant_reference=db.Column(db.String(140))
    plant_grower=db.Column(db.Integer, db.ForeignKey('user.id'))

class Flowerpot(UserMixin, db.Model):
    id=db.Column(db.Integer,primary_key=True)
    flowerpot_location=db.Column(db.String(140))
    planted_plant_id=db.Column(db.Integer, db.ForeignKey('plant.id'))
    


@login.user_loader
def load_user_by_id(id):
    return User.query.get(int(id))
    
    