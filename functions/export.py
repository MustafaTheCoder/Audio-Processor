# Filter the beat at 3kHz
filtered = beat.low_pass_filter(3000)
# Mix loop2 with a reversed, panned version
loop = loop2.reverse().pan(-0.5).overlay(loop2.pan(0.5))
# Mix our filtered beat with the new loop at -3dB
final = filtered.overlay(loop2 - 3, loop=True)

final.export("final.mp3", format="mp3")
