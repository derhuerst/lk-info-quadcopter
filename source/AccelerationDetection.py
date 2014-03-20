from collections import deque

class AccelerationDetection(EventEmitter):
	mean = 1
	meanThreshold = 0.025
	variance = 0
	varianceThreshold = 0.001
	ringBuffer = null
	active = True
	def __init__(**options):
		if 'mean' in options:
			self.mean = options.mean
		if 'meanThreshold' in options:
			self.meanThreshold = options.meanThreshold
		if 'variance' in options:
			self.variance = options.variance
		if 'varianceThreshold' in options:
			self.varianceThreshold = options.varianceThreshold
		self.ringBuffer = deque(maxlen = options.bufferLength if '(bufferLength' in options) else 15)
		if 'active' in options:
			self.active = options.active
class FallDetection(AccelerationDetection):
	pass
class LandDetection(AccelerationDetection):
	pass