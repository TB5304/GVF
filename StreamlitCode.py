#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import math
S = float(st.text_input("Enter the slope (S): "))
Yn = float(st.text_input("Enter the normal depth (Yn): "))
B = float(st.text_input("Enter the width (B): "))
n = float(st.text_input("Enter the Manning's roughness coefficient (n): "))
S0 = float(st.text_input("Enter the bottom slope (S0): "))
Y = float(st.text_input("Flow Depth (Y): "))
def calculate(S,Yn,B,n,S0,Y):
    t = 1
    shape = 'NA'
    if float(S) == 0.000:
        shape = 'Rectangle'
    elif B == 0:
        shape = 'Triangle'
    else:
        shape = 'Trapezoid'
    
    if t:
        if shape == 'Rectangle':
            A = B * Yn
            P = B + 2 * Yn
            R = A / P
            Q = (1/n) * (A) * (R**(2/3)) * (math.sqrt(S0))
            q = Q / B
            Yc = ((q ** 2 )/ (9.81)) ** (1 / 3)
        
        elif shape == 'Triangle':
            A = S*(Yn**2)
            P = (2 * Yn )* math.sqrt(1 +( S ** 2))
            R = A / P
            Q = (1/n) * (A) * (R**(2/3)) * (math.sqrt(S0))
            q = Q / 2
            Yc = ((2*(Q**2))/(9.81*(S**2)))**(1/5)
            
        elif shape == 'Trapezoid':
            A = (B + S * Yn) * Yn
            P = B + (2 * Yn) * (math.sqrt(1 +(S ** 2)))
            R = A / P
            Q = (1/n) * (A) * (R**(2/3)) * (math.sqrt(S0))
            q = Q / B
            Yc = ((q**2)/9.81) ** (1/3)

    if Yn > Yc:
        stype = "Mild"
    elif Yn < Yc:
        stype = "Steep"
    else:
        stype = "Critical"
        
    Y0 = Yn
    if stype == "Mild" or stype == "Steep":
        if Y > Y0 and Y0 > Yc:
            region = 1
        elif Y0 > Y and Y > Yc:
            region = 2
        else:
            region = 3 
        curve = stype[0] + str(region)
    else:
        if Y > Y0 and Y0 == Yc:
            region = 1
        elif Y < Y0 and Y0 == Yc:
            region = 3
            curve = stype[0] + str(region)
        else:
            curve = ""
    
    st.write('Shape =', shape)
    st.write("Area = {:.2f}".format(A))
    st.write("Wetted perimeter = {:.2f}".format(P))
    st.write("Hydraulic radius = {:.2f}".format(R))
    st.write("Discharge = {:.2f}".format(Q))
    st.write("Unit discharge = {:.2f}".format(q))
    st.write("Critical depth = {:.2f}".format(Yc))
    st.write("Slope Type= ",st)
    st.write("Curve Type= ",curve)
calculate(S,Yn,B,n,S0,Y)
