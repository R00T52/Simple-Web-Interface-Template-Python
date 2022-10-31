import sqlite3
import os
import getpass

error = 0
success = 1

#NAME PC USER
USER_NAME = getpass.getuser()

db = sqlite3.connect('C:\\Users\\' + USER_NAME + '\\AppData\\Roaming\\' + '\\data.db')
cur = db.cursor()

admin_login='admin'
admin_password='admin'


def create():
	cur.executescript("""CREATE TABLE IF NOT EXISTS "users" (login TEXT,password TEXT);""")
	db.commit()

def create_admin(admin_login,admin_password):
	cur.execute("INSERT INTO 'users' (login, password) VALUES (?, ?)", (admin_login, admin_password))
	db.commit()

def register_get(login):
    with db:
        result = cur.execute('SELECT login FROM users WHERE login = ?', (login,)).fetchmany(1)
        var = bool(len(result))
        return var

def admin(admin_login):
	if not register_get(admin_login):
		create_admin(admin_login, admin_password)

def password_get(login,password):
	result = cur.execute("SELECT password FROM users WHERE login = ? AND password = ?", (login, password)).fetchone()
	var = bool(len(result))
	return var

def start_db():
	create()
	if not register_get(admin_login):
		create_admin(admin_login,)
	else:
		pass
	

def create_user(login,password):
	cur.execute('INSERT INTO users (login, password) VALUES (?, ?)', [login, password])
	db.commit()

def login_get(login,password):
	if not register_get(login):
		return error
	else:
		if not password_get(login, password):
			return error
		else:
			return success

def register(login,password):
	if not register_get(login):
		create_user(login, password)
		return success
	else:
		return error