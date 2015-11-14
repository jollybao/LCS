# Jialun Bao
# 11/13/15

import numpy as num
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
#plt.rcParams['animation.ffmpeg_path'] = 'C:/ffmpeg/bin/ffmpeg'
#mywriter = animation.FFMpegWriter()
# invert y axis
plt.gca().invert_yaxis()
ims = []

# load 100 frames of pictures
for i in range(100):
    F = num.loadtxt('FTLE%d.txt'%i) 
    im = plt.imshow(F, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True,
                                repeat_delay=1000)

#ani.save('FTLE.mp4',writer = mywriter)

plt.show()
