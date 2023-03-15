#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import math

def hydraulic_calculator(shape, Y0, B, n, S0):
    if st.button('Calculate'):
        if shape == 'Rectangle':
            yc = 2/3 * Y0
            q = (9.81 * yc**3)**0.5
            Q = B * q
            A = B * yc
            P = B + 2 * yc  # Wetted perimeter
            R = A / P  # Hydraulic radius
            SC = (Q**2 / A**2) * (n**2 / R**(4/3))
            yn = A * R**(2/3) * n / S0**(1/2)

        elif shape == 'Circle':
            yc = Y0 / 2
            q = (2/3 * 9.81 * yc**3)**0.5
            Q = math.pi * yc**2 * q
            A = math.pi * yc**2
            P = 2 * math.pi * yc  # Wetted perimeter
            R = A / P  # Hydraulic radius
            SC = (Q**2 / A**2) * (n**2 / R**(4/3))
            yn = A * R**(2/3) * n / S0**(1/2)

        elif shape == 'Triangle':
            yc = Y0 / 3
            q = (8/27 * 9.81 * yc**3)**0.5
            Q = B * q
            A = B * yc
            P = B + 2 * yc * (1 + (1 + B**2 / (4 * yc**2))**0.5)  # Wetted perimeter
            R = A / P  # Hydraulic radius
            SC = (Q**2 / A**2) * (n**2 / R**(4/3))
            yn = A * R**(2/3) * n / S0**(1/2)

        elif shape == 'Parabola':
            yc = (3 * Y0) / 4
            q = (189/40 * 9.81 * yc**3)**0.5
            Q = (2/3) * B * q
            A = (2/3) * B * yc
            P = (4 * yc * ((1 + B**2 / (4 * yc**2))**0.5 + B**2 / (2 * yc)))  # Wetted perimeter
            R = A / P  # Hydraulic radius
            SC = (Q**2 / A**2) * (n**2 / R**(4/3))
            yn = A * R**(2/3) * n / S0**(1/2)
        elif shape == 'Trapezoid':
            yc = ((Y0 / (2 * S0**0.5)) * ((n**2 * B) / (9.81 * (1 + ((Y0 / B)**2) / 4)**0.5)))**(3/5)
            q = (9.81 * yc**3 / n)**0.5
            Q = yc * (B + yc / S0**0.5) * q
            A = yc * (B + yc / S0**0.5)
            P = B + 2 * yc / (1 + (1 + (Y0 / B)**2 / 4)**0.5)
            R = A / P
            SC = (Q**2 / A**2) * (n**2 / R**(4/3))
            yn = A * R**(2/3) * n / S0**(1/2)
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

            # Determine the water profile
        if GVF_profile == "Mild slope":
                if yn <= yc:
                    water_profile = "M1"
                elif yc < yn < Y0:
                    water_profile = "M2"
                else:
                    water_profile = "M3"
        elif GVF_profile == "Critical slope":
                if yn <= yc:
                    water_profile = "C1"
                elif yc < yn < Y0:
                    water_profile = "C2"
                else:
                    water_profile = "C3"
        elif GVF_profile == "Steep slope":
                if yn <= yc:
                    water_profile = "S1"
                elif yc < yn < Y0:
                    water_profile = "S2"
                else:
                    water_profile = "S3"
        elif GVF_profile == "Adverse slope":
                if yn <= Y0:
                    water_profile = "A1"
                else:
                    water_profile = "A2"
        elif GVF_profile == "Horizontal slope":
                if yn <= Y0:
                    water_profile = "H1"
                else:
                    water_profile = "H2"
        else:
                water_profile = "Error: invalid input"

        # Display results
        st.write('Results:')
        st.write(f'Discharge (Q) = {Q} m^3/s')
        st.write(f'Flow area (A) = {A} m^2')
        st.write(f'Wetted perimeter (P) = {P} m')
        st.write(f'Hydraulic radius (R) = {R} m')
        st.write(f'Normal depth (yn) = {yn} m')
        st.write(f'Critical slope (SC) = {SC}')        
        st.write(f'Reservoir water level (Y0) = {Y0}')
        st.write(f'Critical height (yc) = {yc}')        
        st.write(f'Unit discharge from reservoir (q) = {q}')        
        st.write(f'GVF profile = {GVF_profile}')        
        st.write(f'Water profile = {water_profile}')

# Define app layout
st.title('Hydraulic Calculator')
st.sidebar.header('Input Parameters')
shape = st.sidebar.selectbox('Select channel shape', ['Rectangle', 'Circle', 'Triangle', 'Parabola', 'Trapezoid'])
Y0 = st.sidebar.number_input('Enter depth of flow Y0 (m)', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
B = st.sidebar.number_input('Enter bottom width B (m)', min_value=0.0, max_value=10.0, value=1.0, step=0.1)
n = st.sidebar.number_input('Enter Manning roughness coefficient n', min_value=0.01, max_value=0.1, value=0.03, step=0.001)
S0 = st.sidebar.number_input('Enter channel bed slope S0', min_value=0.0, max_value=0.1, value=0.01, step=0.001) 

hydraulic_calculator(shape, Y0, B, n, S0)

