# Repeat 2 times
loop2 = loop * 2
# Get length in milliseconds
length = len(loop2)
# Set fade time
fade_time = int(length * 0.5)
# Fade in and out
faded = loop2.fade_in(fade_time).fade_out(fade_time)