"""Script de Formulaire Flask
Usage:
======
    python GameForm.py
    Programme python contenant les formulaires pour Flask
"""
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, length
from py.messages import Messages


class LoginForm(FlaskForm):
    pseudo = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), length(min=3, max=8)])
    submit = SubmitField(Messages.login_button)


class AddEmprunt(FlaskForm):
    libelle = StringField(validators=[DataRequired()])
    capitaldepart = IntegerField(validators=[DataRequired()])
    capital = IntegerField(validators=[DataRequired()])
    interet = IntegerField(validators=[DataRequired()])
    date = StringField(validators=[DataRequired()])
    periodicite = IntegerField(validators=[DataRequired()])
    echeance = IntegerField(validators=[DataRequired()])
    preteur = StringField(validators=[DataRequired()])
    submit = SubmitField(Messages.add_button)


class AddUser(FlaskForm):
    firstname = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    telephone = IntegerField(validators=[DataRequired()])
    adresse = StringField(validators=[DataRequired()])
    fonction = StringField(validators=[DataRequired()])
    pseudo = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), length(min=3, max=20)])
    passwordconfirm = PasswordField(validators=[DataRequired(), length(min=3, max=20)])
    email = StringField(validators=[DataRequired()])
    submit = SubmitField(Messages.add_button)

class EditMyProfil(FlaskForm):
    firstname = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    telephone = IntegerField(validators=[DataRequired()])
    adresse = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    submit = SubmitField(Messages.edit_button)

class EditUser(FlaskForm):
    firstname = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    telephone = IntegerField(validators=[DataRequired()])
    adresse = StringField(validators=[DataRequired()])
    fonction = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[length(min=0, max=20)])
    email = StringField(validators=[DataRequired()])
    submit = SubmitField(Messages.edit_button)


class AddCAF(FlaskForm):
    annee = IntegerField(validators=[DataRequired()])
    depenses = IntegerField(validators=[DataRequired()])
    recettes = IntegerField(validators=[DataRequired()])
    submit = SubmitField(Messages.add_button)


class EditCAF(FlaskForm):
    depenses = IntegerField(validators=[DataRequired()])
    recettes = IntegerField(validators=[DataRequired()])
    submit = SubmitField(Messages.edit_button)
