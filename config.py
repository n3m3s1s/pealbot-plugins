# coding: utf-8

"""
:var PATHS: Various paths. I.g. plugins
:var IDENTITY: Identity of the bot as a IRC client
:var HOST: IRC server host as tuple (SERVER, PORT)
:var AUTOJOIN: Channels to autojoin
:var PLUGINS: Autoload these plugins
"""
PATHS = {
	"plugins": "plugins",
}

IDENTITY = {
	'nick': 'Noctor',
	'username': "Noctor",
	'realname': 'realname',
	'password': 'xxXXxxXXxx123',
	'auth': '1',
	'Operator': 'operatorusername',
}

HOST = ('irc.freenode.org', 6667)
AUTOJOIN = ("#channels",)


PLUGINS = (
	'basic.Basic',
	'admin.Admin',
	'aspell.Aspell',
	'reminder.Reminder',
	'greet.Greeter',
	#'quotes.Quotes',
)
