"""
Usage:
======
    python ConfigApp.py
    Programme python contenant une config de Flask
"""


class Config:
    """ Stoque les informations de la base de donnée ainsi qu'une clé secréte """
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'admin'
    MYSQL_PASSWORD = "info"
    MYSQL_DB = 'tresorerie'
