import time


def logging(msg):
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	print "[SP] %s @%s" % (msg, current_time)
