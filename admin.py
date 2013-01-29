# coding: utf-8

"""
Copyright (c) 2012 

Anton Zering <synth@lostprofile.de>
Julian Held <nemesis@creative-heads.org>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from plugin import Plugin

class Admin(Plugin):
	export = ['send', 'op', 'deop', 'hop', 'hdeop', 'voice', 'devoice', 'operator', 'part', 'join', 'kill']

	def __init__(self, bot):
		Plugin.__init__(self, bot)
	
	def on_cmd_op(self, msg, params):
		chan = msg.params[0]
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.opMsg('%s +o %s' % (chan, params))
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')

	def on_cmd_deop(self, msg, params):
		chan = msg.params[0]
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.opMsg('%s -o %s' % (chan, params))
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')

	def on_cmd_hop(self, msg, params):
		chan = msg.params[0]
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.opMsg('%s +h %s' % (chan, params))
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')

	def on_cmd_hdeop(self, msg, params):
		chan = msg.params[0]
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.opMsg('%s -h %s' % (chan, params))
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')

	def on_cmd_voice(self, msg, params):
		chan = msg.params[0]
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.opMsg('%s +v %s' % (chan, params))
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')

	def on_cmd_devoice(self, msg, params):
		chan = msg.params[0]
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.opMsg('%s -v %s' % (chan, params))
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')
	
	def on_cmd_send(self, msg, params):
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.msgStuff(params)

	def on_cmd_operator(self, msg, params):
		chan = msg.params[0]
		sender = msg.nick
		self.bot.msg(chan, "My one and only master is %s!" % (self.bot.config.IDENTITY['Operator']))

	def on_cmd_kill(self, msg, params):
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.quit()
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')

	def on_cmd_part(self, msg, params):
		chan = msg.params[0]
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.part(chan)
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')
	
	def on_cmd_join(self, msg, params):
		chan = msg.params[0]
		if msg.nick == self.bot.config.IDENTITY['Operator']:
			self.bot.join(params)
		else:
			self.bot.msg(chan, 'You`re not my f*cking op! (!operator)')

