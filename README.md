# LCS
Lagragian_Coherent_Structure

This project is about to find Lagragian Coherent Structure of a dynamic system, in this case, Double Gyre. 
First, the finite time lyapunov exponent field was computed using Shadden's method, which sets up a grid 
structure of the field, and then computes the mapping of field using standard RK4 method. All the data were
saved into mapping files.

After that, another program reads those files and computes the spatial jacobian at each point, therefore finds
the Green-Cauchy tensor. The largest eigenvalue of the tensor was computed, and it is essentially the FTLE. 
The following picture is the FTLE filed of the system at time 0.
![alt tag](https://cloud.githubusercontent.com/assets/8973982/11157228/5f1f7ac2-8a1e-11e5-93d7-5409f1fc92eb.png)

To speed up the animation, the FTLE fields were also well saved into different files, which then were read by 
the third program, that makes a small animation of the evolution of the Double Gyre from 0 to 10s, with 10 frames
per second. 

![alt tag](https://cloud.githubusercontent.com/assets/8973982/11161241/7acb7fb0-8a45-11e5-8450-45965b584767.gif)

In addition to LCS, I've also made animation that shows the vector field of the Double Gyre chainging as time
evolves. Interestingly, if one drop couple partiles in the field seprated in small distance, they will very
soon diverges and shows the chaotic pattern of the system.

![alt tag](https://cloud.githubusercontent.com/assets/8973982/11161256/dc7849a0-8a45-11e5-8435-566cacdb1484.gif)
