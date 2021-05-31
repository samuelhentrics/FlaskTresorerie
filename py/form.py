"""Script de Formulaire Flask
Usage:
======
    python GameForm.py
    Programme python contenant les formulaires pour Flask
"""
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, IntegerField, PasswordField, FloatField
from wtforms.validators import DataRequired, length, EqualTo, Optional
from py.messages import Messages


class LoginForm(FlaskForm):
    pseudo = StringField(validators=[DataRequired(message=Messages.data_required)])
    password = PasswordField(validators=[DataRequired(message=Messages.data_required),
                                         length(min=3, max=20, message=Messages.password_len)])
    submit = SubmitField(Messages.login_button)


class AddEmprunt(FlaskForm):
    libelle = StringField(validators=[DataRequired(message=Messages.data_required)])
    capitaldepart = FloatField(validators=[DataRequired(message=Messages.data_required)])
    capital = FloatField(validators=[DataRequired(message=Messages.data_required)])
    interet = FloatField(validators=[DataRequired(message=Messages.data_required)])
    date = StringField(validators=[DataRequired(message=Messages.data_required)])
    periodicite = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    echeance = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    preteur = StringField(validators=[DataRequired(message=Messages.data_required)])
    submit = SubmitField(Messages.add_button)

class EditEmprunt(FlaskForm):
    libelle = StringField(validators=[DataRequired(message=Messages.data_required)])
    capitaldepart = FloatField(validators=[DataRequired(message=Messages.data_required)])
    capital = FloatField(validators=[DataRequired(message=Messages.data_required)])
    interet = FloatField(validators=[DataRequired(message=Messages.data_required)])
    date = StringField(validators=[DataRequired(message=Messages.data_required)])
    periodicite = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    echeance = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    preteur = StringField(validators=[DataRequired(message=Messages.data_required)])
    submit = SubmitField(Messages.add_button)


class AddEmpruntSimulation(FlaskForm):
    libelle = StringField(validators=[DataRequired(message=Messages.data_required)])
    capitaldepart = FloatField(validators=[DataRequired(message=Messages.data_required)])
    tauxr = FloatField(validators=[DataRequired(message=Messages.data_required)])
    date = StringField(validators=[DataRequired(message=Messages.data_required)])
    periodicite = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    echeance = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    preteur = StringField(validators=[DataRequired(message=Messages.data_required)])
    submit = SubmitField(Messages.simulate_button)


class Validate(FlaskForm):
    submit = SubmitField(Messages.add_button)


class AddUser(FlaskForm):
    firstname = StringField(validators=[DataRequired(message=Messages.data_required)])
    lastname = StringField(validators=[DataRequired(message=Messages.data_required)])
    telephone = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    adresse = StringField(validators=[DataRequired(message=Messages.data_required)])
    fonction = StringField(validators=[DataRequired(message=Messages.data_required)])
    pseudo = StringField(validators=[DataRequired(message=Messages.data_required)])
    password = PasswordField(validators=[DataRequired(message=Messages.data_required),
                                         length(min=3, max=20, message=Messages.password_len)])
    passwordconfirm = PasswordField(validators=[DataRequired(message=Messages.data_required),
                                                EqualTo('password', message=Messages.equal_to_password),
                                                length(min=3, max=20, message=Messages.password_len)])
    email = StringField(validators=[DataRequired(message=Messages.data_required)])
    submit = SubmitField(Messages.add_button)


class EditMyProfil(FlaskForm):
    firstname = StringField(validators=[DataRequired(message=Messages.data_required)])
    lastname = StringField(validators=[DataRequired(message=Messages.data_required)])
    telephone = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    adresse = StringField(validators=[DataRequired(message=Messages.data_required)])
    email = StringField(validators=[DataRequired(message=Messages.data_required)])
    oldpassword = PasswordField(validators=[Optional(),
                                            length(min=3, max=20, message=Messages.password_len)])
    newpassword = PasswordField(validators=[Optional(),
                                            length(min=3, max=20, message=Messages.password_len)])
    newpasswordconfirm = PasswordField(validators=[Optional(),
                                                   EqualTo('newpassword', message=Messages.equal_to_password),
                                                   length(min=3, max=20, message=Messages.password_len)])
    submit = SubmitField(Messages.edit_button)


class EditUser(FlaskForm):
    firstname = StringField(validators=[DataRequired(message=Messages.data_required)])
    lastname = StringField(validators=[DataRequired(message=Messages.data_required)])
    telephone = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    adresse = StringField(validators=[DataRequired(message=Messages.data_required)])
    fonction = StringField(validators=[DataRequired(message=Messages.data_required)])
    password = PasswordField(validators=[Optional(), length(min=3, max=20, message=Messages.password_len)])
    email = StringField(validators=[DataRequired(message=Messages.data_required)])
    submit = SubmitField(Messages.edit_button)


class AddCAF(FlaskForm):
    annee = IntegerField(validators=[DataRequired(message=Messages.data_required)])
    depenses = FloatField(validators=[DataRequired(message=Messages.data_required)])
    recettes = FloatField(validators=[DataRequired(message=Messages.data_required)])
    submit = SubmitField(Messages.add_button)


class EditCAF(FlaskForm):
    depenses = FloatField(validators=[DataRequired(message=Messages.data_required)])
    recettes = FloatField(validators=[DataRequired(message=Messages.data_required)])
    submit = SubmitField(Messages.edit_button)
