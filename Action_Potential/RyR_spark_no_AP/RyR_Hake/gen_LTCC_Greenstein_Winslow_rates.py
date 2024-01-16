#!/usr/bin/env python3.4

from numpy import *
import sys
import matplotlib.pyplot as plt

print('      MCell L-Type Calcium Variable Rate generation script\n')
print('                          Salk Institute')
print('                                2018')
print('                           Sophia P. Hirakis')
print('                     Computational Neurobiology Lab')
print('         Advised by Thomas M. Bartol and Terrence J. Sejnowski\n')
print('\n This script is used to generate the variable rates for the \n Kinetic properties of the Cardiac L-Type Calcium Channel model described by \nJ.L. Greenstein and R.L.Winslow BiophysJ Vol 83 (2002) 2918-2945. \n')

if (len(sys.argv)<2):
    print('Usage:  ./script_name.py action_potential.dat \n')
    print('\n     Please provide a data file of ')
    print('    time vs. voltage to be processed ')
    
    exit(1)

input_file = sys.argv[1]
input_data = loadtxt(input_file)
### Data processing ###

## Time
time = reshape(input_data[:,0],(len(input_data),1)) 
xaxis = (time)/1000.0  # converting time from milliseconds to seconds
#xaxis = time  # accept time input in units of seconds
#xaxis[0] = 1e-8 # accept time input in units of milliseconds


## Membrane Voltage 
vm = reshape(input_data[:,1],(len(input_data),1)) #Assume membrane voltage is in units of mV

ts = 1000.0 # convert 1/ms to 1/s

#Alpha parameters
alpha = ts*2.0 * exp(0.012*(vm-35))

a12 = 4 * alpha
z = hstack([xaxis, a12])
savetxt('hva_a12.dat',z,fmt='%.15g')

a23 = 3 * alpha
z = hstack([xaxis, a23])
savetxt('hva_a23.dat',z,fmt='%.15g')

a34 = 2 * alpha
z = hstack([xaxis, a34])
savetxt('hva_a34.dat',z,fmt='%.15g')

a45 = alpha
z = hstack([xaxis, a45])
savetxt('hva_a45.dat',z,fmt='%.15g')



#Alpha prime parameters
a = 2.0

a78 = a * 4 *  alpha
z = hstack([xaxis, a78])
savetxt('hva_a78.dat',z,fmt='%.15g')

a89 = a * 3 * alpha
z = hstack([xaxis, a89])
savetxt('hva_a89.dat',z,fmt='%.15g')

a910 = a * 2 * alpha
z = hstack([xaxis, a910])
savetxt('hva_a910.dat',z,fmt='%.15g')

a1011 = a * alpha
z = hstack([xaxis, a1011])
savetxt('hva_a1011.dat',z,fmt='%.15g')




#Beta parameters
beta = ts*0.0882 * exp(-0.05*(vm-35))

b21 = beta
z = hstack([xaxis, b21])
savetxt('hva_b21.dat',z,fmt='%.15g')

b32 = 2 * beta
z = hstack([xaxis, b32])
savetxt('hva_b32.dat',z,fmt='%.15g')

b43 = 3 * beta
z = hstack([xaxis, b43])
savetxt('hva_b43.dat',z,fmt='%.15g')

b54 = 4 * beta
z = hstack([xaxis, b54])
savetxt('hva_b54.dat',z,fmt='%.15g')




#Beta prime parameters
b = 1.9356


b87 = beta/b
z = hstack([xaxis, b87])
savetxt('hva_b87.dat',z,fmt='%.15g')

b98 = 2 * beta/b
z = hstack([xaxis, b98])
savetxt('hva_b98.dat',z,fmt='%.15g')

b109 = 3 * beta/b
z = hstack([xaxis, b109])
savetxt('hva_b109.dat',z,fmt='%.15g')

b1110 = 4 * beta/b
z = hstack([xaxis, b1110])
savetxt('hva_b1110.dat',z,fmt='%.15g')

y_inf = (0.4/(1.0 + exp((vm+12.5)/5.0))) + 0.6
tau_y = (340.0/(1.0 + exp((vm+30.0)/12.0))) + 60.0

k_fy = 1000*y_inf/tau_y
z = hstack([xaxis, k_fy])
savetxt('k_fy.dat',z,fmt='%.15g')

k_by = 1000*(1-y_inf)/tau_y
z = hstack([xaxis, k_by])
savetxt('k_by.dat',z,fmt='%.15g')

# Constants  for IV curve and Flux
P_CaL = 9.13e-13 # cm3/s LTCC channel permeability to Ca2+ (unitary)
P_CaL_L = 9.13e-13/1000. # L/s LTCC channel permeability to Ca2+ (unitary)
T = 310 # K
F = 96.485# C/mmol
R = 8.314 # J/mol K  also CV/mol K
Na_mmol = 0.001*6.02214e23 # Avogadro's Number in mmol

# Inward Ca flux through LTCC assuming 2mM extracellular Ca
J_in = (2)*(Na_mmol/2)*(P_CaL_L*4*vm*F*0.341)/(R*T*(exp((2*vm*F)/(R*T)) - 1))
z = hstack([xaxis,J_in])
savetxt('hva_IV_in.dat',z,fmt='%.15g')


# Bimolecular rate constant for outward Ca flux through LTCC
k_J_out = (Na_mmol/2)*(P_CaL_L*4*vm*F*exp(2*vm*F/(R*T)))/(R*T*(exp((2*vm*F)/(R*T)) - 1))
z = hstack([xaxis,k_J_out])
savetxt('hva_k_IV_out.dat',z,fmt='%.15g')

