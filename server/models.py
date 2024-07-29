from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    date_of_birth = db.Column(db.Integer)
    profile_picture = db.Column(db.String)

    # Relationships
    employments = db.relationship('Employment', backref='user', lazy=True)
    applications = db.relationship('Application', backref='user', lazy=True)
    categories = db.relationship('Category', backref='creator', lazy=True)
    social_integrations = db.relationship('SocialIntegration', backref='user', lazy=True)


class Employment(db.Model):
    __tablename__ = 'employment'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text)
    location = db.Column(db.String)
    salary_range = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    category = db.relationship('Category', backref='employments', lazy=True)

class Category(db.Model):
    _tablename_ = 'category'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Relationships
    social_integrations = db.relationship('SocialIntegration', backref='category', lazy=True)


class Application(db.Model):
    _tablename_ = 'application'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    employment_id = db.Column(db.Integer, db.ForeignKey('employment.id'), nullable=False)
    status = db.Column(db.Integer, nullable=False)  # You can define constants for status
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    employment = db.relationship('Employment', backref='applications', lazy=True)


class SocialIntegration(db.Model):
    _tablename_ = 'socialintegration'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    # Relationships
    category = db.relationship('Category', backref='social_integrations', lazy=True)

