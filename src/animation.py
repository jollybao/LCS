# Jialun Bao
# 11/13/15

import numpy as num
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
# movie_maker
#plt.rcParams['animation.ffmpeg_path'] = 'C:/ffmpeg/bin/ffmpeg'
#mywriter = animation.FFMpegWriter()

# rescale ticks
x = [0,100,200,300,395]
y = [0,100,195]
xlabels = ['0','0.5','1.0','1.5','2.0']
ylabels = ['0','0.5','1.0']


plt.xticks(x,xlabels)
plt.yticks(y,ylabels)
ims = []

# load FTLE data, 100 frames
for i in range(100):
    F = num.loadtxt('FTLE%d.txt'%i) 
    im = plt.imshow(F, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True,
                                repeat_delay=1000)
								
plt.colorbar()								
plt.gca().invert_yaxis()

# make a video
#ani.save('FTLE.mp4',writer = mywriter)

plt.show()
