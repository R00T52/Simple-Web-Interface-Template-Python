import eel
from data import data

error = 0

def start():
	data.start_db()

@eel.expose
def recv_data(login,password):
	if not data.login_get(login, password):
		return error
	else:
		eel.open_main()

@eel.expose
def reg_data(login,password):
	if not data.register(login,password):
		return error
	else:
		eel.open_main()

start()

eel.init("html")
eel.start("Authorization.html", size=(1600, 1200))