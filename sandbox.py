if form_validate.validate_on_submit():
    if request.method == 'POST':
        cur = conn.cursor(dictionary=True, buffered=True)
        capital = capitaldepart/periodicite
        interet = ((1 + tauxr) ** periodicite) - capital
        try:
            cur.execute(
                "INSERT INTO emprunts (libelle, capital_depart, capital,interet,date,periodicite, echeance, preteur)"
                "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    libelle, capitaldepart, capital, interet, date, periodicite, echeance, preteur))
            conn.commit()
            cur.execute("SELECT LAST_INSERT_ID() AS id FROM emprunts")
            last_id = cur.fetchone()
            datecours = date
            restant = int(echeance)
            cur.execute('SELECT MAX(annee) AS annee FROM caf')
            caf_annee_max = cur.fetchone()
            if not caf_annee_max['annee']:
                cur.execute("INSERT INTO caf (annee,depenses,recettes) VALUES ('%s',1,1)" % datetime.now().year)
                conn.commit()
                caf_annee_max = {'annee': datetime.now().year}
            while restant >= 0:
                if restant != 0:
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
            flash(Messages.add_emprunts_validate, 'success')
            return redirect(url_for('emprunts'))
        except:
            flash(Messages.add_emprunts_error, 'warning')
            conn.rollback()
            return redirect(url_for('emprunts'))