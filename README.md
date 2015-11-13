# LCS
Lagragian_Coherent_Structure

This project is about to find Lagragian Coherent Structure of a dynamic system, in this case, Double Gyre. 
First, the finite time lyapunov exponent field was computed using Shadden's method, which sets up a grid 
structure of the field, and then computes the mapping of field using standard RK4 method. All the data were
saved into mapping files.

After that, another program reads those files and computes the spatial jacobian at each point, therefore finds
the Green-Cauchy tensor. The largest eigenvalue of the tensor was computed, and it is essentially the FTLE. 

To speed up the animation, the FTLE fields were also well saved into different files, which then were read by 
third program, that makes a small animation of the evolution of the Double Gyre from 0 to 10s, with 10 frames
per second.

In addition to LCS, I've also made animation that shows the vector field of the Double Gyre chainging as time
evolves. Interestingly, if one drop couple partiles in the field seprated in small distance, they will very
soon diverges and shows the chaotic pattern of the system.
