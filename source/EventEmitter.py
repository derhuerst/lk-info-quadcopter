#!/usr/bin/env python

# Papion
# An API to control the Crazyflie nanocopter.
# Copyright (c) 2014 Jannis R <mail@jannisr.de>
# Released under LGPLv3

"""
`EventEmitter` provides a simple binding and unbinding mechanism. You can listen to events once and continuously. You can also emit an emit, which causes all event handlers to be called.
"""

__author__ = 'Jannis R <mail@jannisr.de>'
__copyright__ = 'Copyright (c) 2014 Jannis R'
__license__ = 'LGPLv3'




# load dependencies
import logging




class EventEmitter(object):


	"""
	In `handlers`, all event handlers are stored, sorted by event name. Each event has a separate array in `handlers`.
	"""
	handlers = {}
	"""
	Structurally, `handlersOnce` is equal to `handlers`. However, in `handlersOnce`, for each event handler in `handlers`, a `True`or `False`is stored. If `True`is sorted the event handler will be removed once executed.
	"""
	handlersOnce = {}


	def on(self, event, handler, once = False):

		"""
		`on` adds `handler` to the list of handlers for `event`. `handler` will be executed everytime `event` is emitted.
		"""

		# check self.handlers and self.handlersOnce
		if not event in self.handlers:
			self.handlers[event] = []
		if not event in self.handlersOnce:
			self.handlersOnce[event] = []

		# append handler if not in list
		if not handler in self.handlers[event]:
			self.handlers[event].append(handler)
			self.handlersOnce[event].append(once)


	def once(self, event, handler):

		"""
		`once` adds `handler` to the list of handlers for `event`. `handler` will be executed only *once*.
		"""

		# call self.on with `once = True`
		return self.on(event, handler, True)


	def off(self, event, handler):

		"""
		`off` removes `handler`  from the list of handlers for `event`
		"""

		# check self.handlers
		if (not event in self.handlers) or (len(self.handlers) == 0):
			raise Exception('no handlers for event ' + str(event))
		if not handler in self.handlers[event]:
			raise Exception('no such handler for event ' + str(event))

		# find an remove handler
		i = self.handlers[event].index(handler)
		self.handlers[event].pop(i)
		self.handlersOnce[event].pop(i)


	def emit(self, event, data):

		"""
		`emit` calls all handlers for `event` and passes `data` as a parameter.
		"""

		# logging
		logging.debug('emmitting event `' + str(event) + '`')

		# check self.handlers
		if not event in self.handlers:
			return

		# loop through self.handlers[event] and call every handler
		i = 0
		for handler in self.handlers[event]:
			if self.handlersOnce[event][i]:
				self.handlers[event].pop(i)
				self.handlersOnce[event].pop(i)
			try:
				handler(data)
			except:
				handler({})
		i += 1




logging.debug('module EventEmitter loaded')