# -*- coding:utf-8 -*-
"""
Usage:
======
    python app.py
    Programme python (Application) principale pour lancer Flask
"""
import math
import MySQLdb
from flask import Flask, render_template, redirect, flash, url_for, request, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import ConfigApp
from py.form import LoginForm, AddUser, AddEmprunt, EditUser, AddCAF, EditCAF
from py.messages import Messages
import locale
import calendar
from datetime import date
from dateutil.relativedelta import relativedelta

__authors__ = ("Samuel HENTRICS", "Julen ELizalde")
__contact__ = ("samuel.hentrics@gmail.com",
               "hentrics.samuel@ent-st-joseph-hasparren.fr",
               "elizalde.julen@ent-st-joseph-hasparren.fr",
               "julen.elizalde1@gmail.com")
__paypal__ = ("Paypal Julen: paypal.me/Goldenhunter264,"
              "Paypal Samuel: paypal.me/SamuelHentrics")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "21/08/02"

app = Flask(__name__)
bdd = ConfigApp.Config()  # création de l'objet bdd
app.secret_key = bdd.SECRET_KEY  # clé secrète
conn = mysql.connector.connect(host=bdd.MYSQL_HOST,
                               user=bdd.MYSQL_USER,
                               password=bdd.MYSQL_PASSWORD,
                               database=bdd.MYSQL_DB)
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')


# Accueil

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html.jinja', nom_ville=Messages.ville_name)


# Login

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST' and 'pseudo' in request.form and 'password' in request.form:
        pseudo = request.form['pseudo']
        password = request.form['password']
        cur = conn.cursor(dictionary=True)
        cur.execute('SELECT * FROM users WHERE pseudo = %s', (pseudo,))
        data = cur.fetchone()
        if check_password_hash(data["password"], password):
            session['loggedin'] = True
            session['user'] = data
            flash(Messages.login_success, 'success')
            return redirect(url_for('home'))
        else:
            flash(Messages.incorrect_password, 'warning')
    return render_template('security/login.html.jinja', form=form)


@app.route('/logout')
def logout():
    if 'loggedin' in session:
        session.pop('loggedin', None)
        session.pop('user', None)
        flash(Messages.logout_success, 'warning')
    return redirect(url_for('home'))


# Emprunts

@app.route('/emprunts', defaults={'page': 1})
@app.route('/emprunts/pages/<int:page>')
def emprunts(page):
    if 'loggedin' in session:
        limit = 5
        offset = page * limit - limit
        cur = conn.cursor(buffered=True, dictionary=True)
        cur.execute('SELECT * FROM details_emprunts GROUP BY YEAR(date)')
        total_row = cur.rowcount
        total_page = math.ceil(total_row / limit)
        prev = page - 1
        next = page + 1
        cur.execute('SELECT YEAR(de.date) AS date, SUM(e.capital) AS capital, SUM(e.interet) AS interet '
                    'FROM details_emprunts de '
                    'INNER JOIN emprunts e '
                    'ON e.id=de.emprunt_id '
                    'GROUP BY YEAR(de.date) '
                    'LIMIT %s OFFSET %s', (limit, offset,))
        data = cur.fetchall()
        return render_template('emprunts/annee.html.jinja', emprunts=data, page=page,
                               maximum=total_page,
                               pages=range(1, int(total_page) + 1), next=next,
                               prev=prev)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/emprunts/liste')
def emprunts_list():
    if 'loggedin' in session:
        cur = conn.cursor(dictionary=True)
        cur.execute('SELECT * '
                    'FROM emprunts '
                    'ORDER BY YEAR(date)')
        data = cur.fetchall()
        return render_template('emprunts/liste.html.jinja', emprunts=data, )


@app.route('/emprunts/delete/<int:id>')
def delete_emprunt(id):
    cur = conn.cursor()
    cur.execute('DELETE FROM emprunts WHERE id = {0}'.format(id))
    conn.commit()
    cur.execute('DELETE FROM details_emprunts WHERE emprunt_id ={0}'.format(id))
    conn.commit()
    flash('Cet emprunt a été supprimé', 'success')
    return redirect(url_for('emprunts_list'))


@app.route('/emprunts/<int:annee>')
def emprunts_annee(annee):
    if 'loggedin' in session:
        cur = conn.cursor(dictionary=True)
        data={}
        for i in range(1,13):
            print(i)
            cur.execute(
                'SELECT e.libelle AS libelle, e.capital AS capital, e.interet AS interet, e.date AS date, e.periodicite AS periodicite, de.restant AS restant, e.echeance AS echeance, e.preteur AS preteur '
                'FROM details_emprunts de '
                'INNER JOIN emprunts e '
                'ON e.id=de.emprunt_id '
                'WHERE YEAR(de.date)=%s AND MONTH(de.date)=%s'
                , (annee, i,))
            data[calendar.month_name[i].capitalize()] = cur.fetchall()
        print(data)
        return render_template('emprunts/details_annee.html.jinja', data=data,
                               annee=annee)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/emprunts/add', methods=['GET', 'POST'])
def add_emprunt():
    if 'loggedin' in session:
        error = None
        form = AddEmprunt()
        if form.validate_on_submit():
            if request.method == 'POST':
                libelle = request.form['libelle']
                capitaldepart = request.form['capitaldepart']
                capital = request.form['capital']
                interet = request.form['interet']
                datedebut = request.form['date']
                periodicite = request.form['periodicite']
                echeance = request.form['echeance']
                preteur = request.form['preteur']
                cur = conn.cursor(buffered=True, dictionary=True)
                try:
                    cur.execute(
                        "INSERT INTO emprunts (libelle, capital_depart, capital,interet,date,periodicite, echeance, preteur)"
                        "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            libelle, capitaldepart, capital, interet, datedebut, periodicite, echeance, preteur))
                    conn.commit()
                    cur.execute("SELECT LAST_INSERT_ID() AS id FROM emprunts")
                    last_id = cur.fetchone()
                    datecours = datedebut
                    restant = int(echeance)
                    cur.execute('SELECT MAX(annee) AS annee FROM caf')
                    caf_annee_max = cur.fetchone()
                    while restant >= 0:
                        cur.execute(
                            "INSERT INTO details_emprunts (date,emprunt_id,restant) "
                            "VALUES ('%s','%s','%s')" % (
                                datecours, last_id['id'], restant))
                        conn.commit()
                        datecours = date.fromisoformat(datecours) + relativedelta(months=int(periodicite))
                        cur.execute('SELECT annee FROM caf WHERE annee=%s', (int(datecours.strftime('%Y')),))
                        exist = cur.fetchone()
                        if not exist:
                            cur.execute("INSERT INTO caf (annee, recettes, depenses)"
                                        "VALUES ('%s', '%s', '%s')" %
                                        (int(datecours.strftime('%Y')) - 1, 0, 0))
                            if int(datecours.strftime('%Y')) > caf_annee_max['annee'] and restant == 0:
                                cur.execute("INSERT INTO caf (annee, recettes, depenses)"
                                            "VALUES ('%s', '%s', '%s')" %
                                            (int(datecours.strftime('%Y')), 0, 0))
                        datecours = datecours.strftime('%Y-%m-%d')
                        restant = restant - 1
                    flash("Emprunt ajouté", 'success')
                    return redirect(url_for('emprunts'))
                except:
                    flash("L'emprunt n'a pas été ajouté", 'warning')
                    conn.rollback()
                    return redirect(url_for('emprunts'))
        return render_template('emprunts/add.html.jinja', form=form, error=error)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/emprunts/edit', methods=['GET', 'POST'])
def edit_emprunt():
    if 'loggedin' in session:
        return render_template('emprunts/edit.html.jinja')
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


# CAF

@app.route('/caf')
def caf():
    if 'loggedin' in session:
        cur = conn.cursor(dictionary=True)
        cur.execute('SELECT * FROM caf GROUP BY annee')
        caf = cur.fetchall()
        for i in range(len(caf)):
            caf[i]['ebf'] = caf[i]['recettes'] - caf[i]['depenses']
            cur.execute('SELECT SUM(e.capital) AS capital, SUM(e.interet) AS interet '
                        'FROM emprunts e '
                        'INNER JOIN details_emprunts de '
                        'ON de.emprunt_id=e.id '
                        'WHERE YEAR(de.date)=%s', (int(caf[i]['annee']),))
            emprunts = cur.fetchone()
            print(emprunts)
            if emprunts['capital'] == None or emprunts['interet'] == None:
                caf[i]['annuite'] = "Manque de données"
                caf[i]['caf'] = "Manque de données"
            else:
                caf[i]['annuite'] = emprunts['capital'] + emprunts['interet']
                caf[i]['caf'] = caf[i]['recettes'] - caf[i]['depenses'] - caf[i]['annuite']
        return render_template('caf/index.html.jinja', caf=caf)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/caf/edit', methods=['GET', 'POST'])
def add_caf():
    if 'loggedin' in session:
        error = None
        form = AddCAF()
        if form.validate_on_submit():
            if request.method == 'POST':
                annee = request.form['annee']
                depenses = request.form['depenses']
                recettes = request.form['recettes']
                cur = conn.cursor()
                cur.execute("SELECT annee FROM caf WHERE annee=%s", (annee,))
                data = cur.fetchall()
                if data:
                    error = "L'année est déjà renseignée"
                    return render_template('caf/add.html.jinja', form=form, error=error)
                else:
                    try:
                        cur.execute(
                            "INSERT INTO caf (annee,depenses,recettes) VALUES ('%s','%s','%s')" % (
                                annee, depenses, recettes))
                        conn.commit()
                        flash("CAF ajoutée", 'success')
                        return redirect(url_for('caf'))
                    except:
                        flash("CAF non ajoutée", 'warning')
                        conn.rollback()
                        return redirect(url_for('caf'))
        return render_template('caf/add.html.jinja', form=form, error=error)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/caf/edit/<int:annee>', methods=['GET', 'POST'])
def edit_caf(annee):
    if 'loggedin' in session:
        error = None
        form = EditCAF()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT recettes, depenses "
                    "FROM caf WHERE annee = %s", (annee,))
        data = cur.fetchone()
        if form.validate_on_submit():
            if request.method == 'POST':
                depenses = request.form['depenses']
                recettes = request.form['recettes']
                try:
                    cur.execute("UPDATE caf "
                                "SET depenses= %s,recettes = %s"
                                "WHERE annee=%s",
                                (depenses, recettes, annee))
                    conn.commit()
                    flash("L'année a été modifiée", 'success')
                    return redirect(url_for('caf'))
                except:
                    flash("CAF non modifiée", 'warning')
                    conn.rollback()
                    return redirect(url_for('caf'))
        return render_template('caf/edit.html.jinja', form=form, error=error, caf=data, annee=annee)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/caf/delete/<int:annee>')
def delete_caf(annee):
    cur = conn.cursor()
    cur.execute('DELETE FROM caf WHERE annee = {0}'.format(annee))
    conn.commit()
    flash('Cette année a été supprimé', 'success')
    return redirect(url_for('caf'))


# PROFIL

@app.route('/profil')
def profil():
    if 'loggedin' in session:
        return render_template('profil/settings.html.jinja')
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/profil/list', defaults={'page': 1})
@app.route('/profil/list/<int:page>')
def profil_list(page):
    if 'loggedin' in session:
        if session['user']['admin'] == 1:
            limit = 8
            offset = page * limit - limit
            cur = conn.cursor(buffered=True, dictionary=True)
            cur.execute('SELECT pseudo '
                        'FROM users')
            total_row = cur.rowcount
            total_page = math.ceil(total_row / limit)
            prev = page - 1
            next = page + 1
            cur.execute('SELECT avatar, firstname,lastname, pseudo, fonction, email, id, admin '
                        'FROM users LIMIT %s OFFSET %s',
                        (limit, offset,))
            data = cur.fetchall()
            return render_template('profil/list.html.jinja', users=data, page=page,
                                   maximum=total_page,
                                   pages=range(1, int(total_page) + 1), next=next,
                                   prev=prev)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/profil/add', methods=['GET', 'POST'])
def profil_add():
    if 'loggedin' in session:
        if session['user']['admin'] == 1:
            error = None
            form = AddUser()
            if form.validate_on_submit():
                if request.method == 'POST':
                    firstname = request.form['firstname']
                    lastname = request.form['lastname']
                    fonction = request.form['fonction']
                    telephone = request.form['telephone']
                    adresse = request.form['adresse']
                    pseudo = request.form['pseudo']
                    password = request.form['password']
                    passwordconfirm = request.form['passwordconfirm']
                    email = request.form['email']
                    admin = 0
                    cur = conn.cursor()
                    cur.execute("SELECT pseudo FROM users WHERE pseudo=%s", (pseudo,))
                    data = cur.fetchall()
                    if data:
                        error = "Le pseudo ou l'email est déjà utilisé"
                        return render_template('profil/add.html.jinja', form=form, error=error)
                    elif password != passwordconfirm:
                        error = "La confirmation du mot de passe a échoué"
                        return render_template('profil/add.html.jinja', form=form, error=error)
                    else:
                        try:
                            password = generate_password_hash(password)
                            cur.execute(
                                "INSERT INTO users (firstname,lastname,fonction,telephone,adresse,pseudo,password,email"
                                ",admin) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                    firstname, lastname, fonction, telephone, adresse, pseudo, password, email, admin))
                            conn.commit()
                            flash("Utilisateur ajouté", 'success')
                            return redirect(url_for('profil_list'))
                        except:
                            flash("L'utilisateur n'a pas été ajouté", 'warning')
                            conn.rollback()
                            return redirect(url_for('profil_list'))
            return render_template('profil/add.html.jinja', form=form, error=error)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/profil/list/edit/<int:id>', methods=['GET', 'POST'])
def profil_edit(id):
    if 'loggedin' in session:
        if session['user']['admin'] == 1:
            error = None
            form = EditUser()
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT id, email, pseudo, firstname, lastname, fonction, telephone, adresse, admin "
                        "FROM users WHERE id = %s", (id,))
            data = cur.fetchone()
            if form.validate_on_submit():
                if request.method == 'POST':
                    firstname = request.form['firstname']
                    lastname = request.form['lastname']
                    fonction = request.form['fonction']
                    telephone = request.form['telephone']
                    adresse = request.form['adresse']
                    password = request.form['password']
                    email = request.form['email']
                    admin = 0
                    try:
                        cur.execute("""UPDATE users
                                        SET email = %s,firstname = %s,
                                        lastname =%s,fonction = %s,telephone = %s,adresse = %s
                                        WHERE id = %s""", (email, firstname,
                                                           lastname, fonction, telephone, adresse, id))
                        conn.commit()
                        flash("L'utilisateur a été modifié", 'success')
                        return redirect(url_for('profil_list'))
                    except:
                        flash('Erreur | L\'utilisateur n\'a pas été modifié', 'warning')
                        conn.rollback()
                        return render_template('profil/edit.html.jinja', data=data[0], form=form, error=error)
            return render_template('profil/edit.html.jinja', data=data, form=form, error=error)
    else:
        flash(Messages.need_login, "warning")
        return redirect(url_for('login'))


@app.route('/profil/user/delete/<int:id>')
def profil_delete(id):
    cur = conn.cursor()  # on
    cur.execute('DELETE FROM users WHERE id = {0}'.format(id))
    conn.commit()
    flash('L\'utilisateur a été supprimé', 'success')
    return redirect(url_for('user_list'))


# Calendrier

@app.route('/calendar')
def calendrier():
    return render_template('calendar/index.html.jinja')


"""Déclaration des pages d'erreur classiques : 403, 404 et 500"""


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('security/403.html.jinja'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('security/404.html.jinja'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('security/500.html.jinja'), 500
