import math
import streamlit as st

def calculate(S, Yn, B, n, S0, Y, UOD='NA', P=10):

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
        slope_type = "Mild"
    elif Yn < Yc:
        slope_type = "Steep"
    else:
        slope_type = "Critical"
    Y0=Yn
    if slope_type == "Mild" or slope_type == "Steep":
        if Y > Y0 and Y0 > Yc:
            Region = 1
        elif Y0 > Y and Y > Yc:
            Region = 2
        else:
            Region = 3
        curve = slope_type[0] + str(Region)
    else:
        if Y > Y0 and Y0 == Yc:
            Region = 1
        elif Y < Y0 and Y0 == Yc:
            Region = 3
    curve = slope_type[0] + str(Region)

    st.write('Shape =', shape)
    st.write("Area = {:.2f}".format(A))
    st.write("Wetted perimeter = {:.2f}".format(P))
    st.write("Hydraulic radius = {:.2f}".format(R))
    st.write("Discharge = {:.2f}".format(Q))
    st.write("Unit discharge = {:.2f}".format(q))
    st.write("Critical depth = {:.2f}".format(Yc))
    st.write("Slope Type =", slope_type)
    st.write("Curve Type =", curve)

    ####################################GVF Length Calculation###########################
    ## Calculating Middle Value
    if UOD == 'Upstream':
        P = 1 + P // 100
    elif UOD == 'Downstream':
        P = 1 - P // 100
    else:
        if int(curve[-1]) == 1 or int(curve[-1]) == 3:
            P = 1 + P // 100
        else:
            P = 1 - P // 100
    ed = Yn * P
    XXM = [Y, float((ed + Y) / 2), ed]
    st.write(XXM)
    flag = 0
    E = 0
    for i in range(3):
        Yn = XXM[i]

        if shape == 'Rectangle':
            A = B * Yn
            P = B + 2 * Yn
            R = A / P

        elif shape == 'Triangle':
            A = S*(Yn**2)
            P = (2 * Yn )* math.sqrt(1 +( S ** 2))
            R = A / P

        else:
            A = (B + S * Yn) * Yn
            P = B + (2 * Yn) * (math.sqrt(1 +(S ** 2)))
            R = A / P
        V = Q / A
        ## TO Store Prev Values In Variables
        if i > 0:
            PE = E
            PSf = Sf
            if i > 1:
                PL = L
        ## To Use Values Into Real Application
        E = (Yn + (V ** 2) / (2 * 9.81))
        Sf = ((V * n) / (R ** (2 / 3))) ** 2
        if i > 0:
            DE = E - PE  ## Delta E
            MSf = ((Sf + PSf) / 2)  ## Mean Sf
            S0_Sf = S0 - MSf
            DX = DE / S0_Sf
            if i == 1:
                L = -DX
            else:
                L = PL - DX
    if st.button("Calculate"):
        calculate(S, Yn, B, n, S0, Y, UOD, P)
def main():
    st.title("Hydraulic Calculations")
    S = st.sidebar.number_input("Slope (S)", value=0.000)
    Yn = st.sidebar.number_input("Normal Depth (Yn)", value=2.0)
    B = st.sidebar.number_input("Bottom Width (B)", value=3.0)
    n = st.sidebar.number_input("Manning's Roughness Coefficient (n)", value=0.05)
    S0 = st.sidebar.number_input("Channel Bed Slope (S0)", value=1.5)
    Y = st.sidebar.number_input("Flow Depth (Y)", value=1.2)
    UOD = st.sidebar.selectbox("Upstream or Downstream (UOD)", ["NA", "Upstream", "Downstream"])
    P = st.sidebar.number_input("Percentage Change in Perimeter (P)", value=10)

    calculate(S, Yn, B, n, S0, Y, UOD, P)

if __name__ == '__main__':
    main()
