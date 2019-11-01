#!/usr/bin/env python
# -*- coding: UTF-8 -*-
welcome= """
___________________________________________________________________________________
S I M P L E   R A N D O M   S A M P L I N G   P R O G R A M 
                                   Version: (P).1.1
by Tülin (Otbiçer) ACAR \u00A9 2019 (P)arantez Education Research Consultancy and Publishing
https://parantezanaliz.com & totbicer@gmail.com
____________________________________________________________________________________"""
print(welcome)
universe = input("1# The size of the universe defined and limited (N) : ")
while True:
        if universe.isdigit() and int(universe)>0:
                break
        else:
                print("You logged in incorrectly. You must enter a naturel number greater than zero.")
                universe = input("1# The size of the universe defined and limited (N) : ")
        
                                        
error = input("2# Sampling error (c = ± ): ")
while True:
        if error.isdigit() and 0<int(error)<100:
             break        
        else:
                print("Ooops! Enter an error between 1 and 100 (e.g. 5) as a a naturel number.")
                error = input("2# Sampling error (c = ± ): ")

confidence = input("3# Confidence interval (%) : ")
while True:
        if confidence.isdigit() and int(confidence)==95:
            z=1.96
            break
        if confidence.isdigit() and int(confidence)==99:
            z=2.58
            break
        else:
                    print("For confidence interval, enter either 95 or 99 as a a naturel number!")
                    confidence = input("3# Confidence interval (%) : ")

prob = input("4# You describe the probability of being involved or the event or the rate of observation. \n     If you have no idea, write 50. P(%) = ")
while True:
        if prob.isdigit() and 0<int(prob)<100:
                break
        else:
                print("It did not. What is the percentage of being / observing? (e.g., 50 percent).")
                prob = input("4# You describe the probability of being involved or the event or the rate of observation. \n If you have no idea, write 50. P(%) = ")

p_ratio=int(prob)/int(100)
q_ratio = (1 - p_ratio)
x = int(error)/int(100)
c        = pow(x,2)
zz       = pow(z,2)
process    = ((zz*(p_ratio*q_ratio))/c)
sample   = int(process)/(1+((int(process)/int(universe))))
sampling = round(sample,0)
ornek = int(sampling)
N=int(universe)

import random
liste = [random.randint(1, N) for i in range(ornek)]


print (" \n >>> C A L C U L A T E D    R E S U L T  <<<\n", "The number of universes", universe, "; sampling error", chr(177) , error, "; confidence interval", confidence,"%.", "\nThe sample size is", sampling, "units. \n \n If you have given sequence numbers to the observations/units in the universe, the randomly selected and ordered sequence numbers of the", sampling, "units of observations/units you can sample are listed below.")
print (sorted(liste), sep="\t")


a = input()

