import numpy as num
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
plt.gca().invert_yaxis()
ims = []

for i in range(20):
    F = num.loadtxt('FTLE%d.txt'%i) 
    im = plt.imshow(F, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True,
                                repeat_delay=1000)

#ani.save('dynamic_images.mp4')

plt.show()
