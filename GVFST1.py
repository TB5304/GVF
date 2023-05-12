#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import math

def hydraulic_calculator(SC, Y0, B, n, S0):
    if st.button('Calculate'):
        ST='NA'
        if SC==0.0000:
            shape='Rectangle'
        elif B==0:
            shape='Triangle'
        else:
            shape='Trapezoid'
        if shape == 'Rectangle':
                A=B*Y0
                P=(B+2*Y0)
                R=(A/P)
                V=(1/n)*(R**(2/3))*(S0**(1/2))
                Q=A*V
                q=Q/B
                Yc=((q**2)/9.81)**(1/3)

        elif shape == 'Triangle':
                A = (B + b) / 2 * Y0
                P = B - b + 2 * ((Y0**2 + (B-b)**2)**0.5)
                R = A / P
                V = (1/n) * (R**(2/3)) * (S0**(1/2))
                Q = A * V
                q = Q / B
                Yc = ((q**2) / (9.81 * P))**(1/3)
        elif shape == 'Trapezoid':
            A = B * Y0 / 2
            P = B + 2 * (Y0**2 + B**2)**0.5
            R = A / (P/2)
            V = (1/n) * (R**(2/3)) * (S0**(1/2))
            Q = A * V
            q = Q / B
            Yc = ((q**2) / (9.81 * B))**(1/3)
        else:
            print("Entered Shape Is Incorrect")
        if SC > S0:
                GVF_profile = "Steep slope"
        elif SC == S0:
                GVF_profile = "Critical slope"
        elif 0 < SC < S0:
                GVF_profile = "Mild slope"
        elif SC == 0:
                GVF_profile = "Horizontal slope"
        elif SC < 0:
                GVF_profile = "Adverse slope"
        else:
                GVF_profile = "Error: invalid input"

        # Display results
        st.write('Results:')
        st.write(f'Shape: {shape}')
        st.write(f'Discharge (Q) = {Q} m^3/s')
        st.write(f'Flow area (A) = {A} m^2')
        st.write(f'Wetted perimeter (P) = {P} m')
        st.write(f'Hydraulic radius (R) = {R} m')
        st.write(f'Critical height (Yc) = {yc}')        
        st.write(f'Unit discharge from reservoir (q) = {q}')        
        st.write(f'GVF profile = {GVF_profile}')        

# Define app layout
st.title('Hydraulic Calculator')
st.sidebar.header('Input Parameters')
SC = st.sidebar.number_input('EnterSide Slope 1:X', min_value=0.0, max_value=1000.0, value=1.0, step=0.1)
Y0 = st.sidebar.number_input('Enter depth of flow Y0 (m)', min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
Q = st.sidebar.number_input('Enter Q', min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
B = st.sidebar.number_input('Enter bottom width B (m)', min_value=0.0, max_value=1000.0, value=1.0, step=0.1)
n = st.sidebar.number_input('Enter Manning roughness coefficient n', min_value=0.01, max_value=10.00, value=0.03, step=0.01)
S0 = st.sidebar.number_input('Enter channel bed slope S0', min_value=0.0001, max_value=100.0000, value=0.0004, step=0.0001)

hydraulic_calculator(SC, Y0, B, n, S0)

