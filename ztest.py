import math
import sqlite3


def twoSampZ(X1, X2, sd1, sd2, n1, n2,alpha,type):
    from numpy import sqrt, abs, round
    from scipy.stats import norm
    import scipy.stats as st
    mudiff=0;
    pasalaPrueba=0;
    pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
    z = ((X1 - X2) - mudiff)/pooledSE
    pval = 2*(1 - norm.cdf(abs(z)))
    zValue=0;

    #Ha: u1 <u2
    if type== "ColaIzquierda":
        zValue = st.norm.ppf(alpha)
        if z < zValue:
            pasalaPrueba=1;
        else:
            pasalaPrueba=0;
    # Ha: u1 > u2
    elif type == "ColaDerecha":
        zValue = st.norm.ppf(1 - alpha)
        if z > zValue:
            pasalaPrueba=1;
        else:
            pasalaPrueba=0;
    # Ha: u1 = u2
    elif type == "DosColas":
        if z >= st.norm.ppf(alpha) and z<= st.norm.ppf(1 - alpha):
            pasalaPrueba=1;
        else:
            pasalaPrueba=0;
    else:
        print("Error tyoe")
    return pasalaPrueba,round(z, 3), round(pval, 4), round(zValue,3)

if __name__ == '__main__':
    siginicantLevel=95;
    alpha=(100-siginicantLevel)/100;
    #alpha=0.05;
    #mu1Promedios=[0.00E+00,2.44E-193,0.00E+00,2.57E-193,1.58E+00,1.48E-07,7.55E-05,-1.26E+04,0.00E+00,8.88E-16,0.00E+00,5.56E-08,2.19E-03,0.00E+00,1.84E-191,0.00E+00,1.68E-189,3.24E+00,6.46E-03,1.47E-04,-4.19E+04,0.00E+00,8.88E-16,0.00E+00,4.95E-05,2.58E-03,0.00E+00,1.14E-188,0.00E+00,1.35E-184,1.69E+00,3.87E-01,1.01E-04,-2.09E+05,0.00E+00,8.88E-16,0.00E+00,1.81E-04,5.74E-02,0.00E+00,1.14E-128,0.00E+00,1.90E-189,1.85E+00,6.77E-01,1.04E-04,-4.19E+05,0.00E+00,8.88E-16,0.00E+00,3.29E-04,1.24E-01]
    #mu2Promedios=[2.97E-212,2.56E-109,1.13E-215,1.66E-107,2.89E+01,6.15E+00,1.92E-04,-5.83E+03,0.00E+00,8.88E-16,0.00E+00,7.77E-01,2.98E+00,1.72E-213,2.13E-105,6.43E-211,3.66E-109,9.89E+01,2.35E+01,1.32E-04,-1.19E+04,0.00E+00,8.88E-16,0.00E+00,1.03E+00,9.99E+00,7.78E-205,6.17E-105,4.91E-210,5.49E-106,498.9411472,1.24E+02,1.37E-04,-2.77E+04,0.00E+00,8.88E-16,0.00E+00,1.16E+00,5.00E+01,4.22E-216,5.93E-03,8.61E-211,8.8881E-107,9.99E+02,2.48E+02,1.36E-04,-3.83E+04,0.00E+00,8.88E-16,0.00E+00,1.17E+00,1.00E+02]
    #mu1Desv=[0.00E+00,0.00E+00,0.00E+00,0.00E+00,6.02E+00,2.38E-07,7.09E-05,1.11E-04,0.00E+00,0.00E+00,0.00E+00,1.12E-07,1.01E-02,0.00E+00,0.00E+00,0.00E+00,0.00E+00,1.73E+01,6.92E-03,1.17E-04,1.67E+00,0.00E+00,0.00E+00,0.00E+00,6.34E-05,4.58E-03,0.00E+00,0.00E+00,0.00E+00,0.00E+00,2.58E+00,5.11E-01,7.58E-05,3.10E+01,0.00E+00,0.00E+00,0.00E+00,2.24E-04,1.02E-01,0.00E+00,0.00E+00,0.00E+00,0.00E+00,3.09E+00,7.02E-01,8.01E-05,2.45E+02,0.00E+00,0.00E+00,0.00E+00,4.11E-04,1.53E-01]
    #mu2Desv=[0.00E+00,7.11E-109,0.00E+00,5.95E-107,2.59E-02,5.16E-01,1.84E-04,7.81E+02,0.00E+00,0.00E+00,0.00E+00,2.19E-01,9.35E-02,0.00E+00,1.17E-104,0.00E+00,1.09E-108,3.74E-02,8.48E-01,1.13E-04,2.07E+03,0.00E+00,0.00E+00,0.00E+00,1.12E-01,3.01E-03,0.00E+00,3.33E-104,0.00E+00,2.60E-105,0.038063727,4.90E-01,1.37E-04,5.64E+03,0.00E+00,0.00E+00,0.00E+00,2.11E-02,4.82E-03,0.00E+00,2.70E-02,0.00E+00,4.6574E-106,3.16E-02,7.72E-01,9.23E-05,7.43E+03,0.00E+00,0.00E+00,0.00E+00,8.74E-03,3.18E-03]
    mu1Promedios=[25.33957835, 13.83241729 ]
    mu2Promedios=[38.4703218,20.96844548]
    mu1Desv=[13.08932372,7.146646896]
    mu2Desv=[18.28508377,9.964167164]
    n1=30
    n2=30
    type="ColaIzquierda"
    #type="ColaDerecha"
    #type="DosColas"

    conn = sqlite3.connect('Z TEST.db')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping EMPLOYEE table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Z_TEST")

    # Creating table as per requirement
    sql = '''CREATE TABLE Z_TEST(ID INT PRIMARY KEY,
                P_U1           DOUBLE    ,
                D_U1            DOUBLE    ,
                P_U2        DOUBLE,
                D_U2        DOUBLE,
                Z DOUBLE ,
                P DOUBLE ,
                Z_VAL DOUBLE ,
                RESULTADO INT 
        );'''
    cursor.execute(sql)

    print("Table created successfully........")
    incremento=1e-15;

    for i in range(len(mu1Promedios)):
        if (mu1Promedios[i]==0):
            mu1Promedios[i]+=incremento
        if (mu2Promedios[i]==0):
            mu2Promedios[i]+=incremento
        if (mu1Desv[i]==0):
            mu1Desv[i]+=incremento
        if (mu2Desv[i]==0):
            mu2Desv[i]+=incremento


        resultado, z, p, zval = twoSampZ(mu1Promedios[i], mu2Promedios[i], mu1Desv[i], mu2Desv[i], n1, n2, alpha, type)
        if resultado == 1:
            print("Hay suficiente evidencia para apoyar la afirmacion")
        else:
            print("No hay suficiente evidencia para apoyar la afirmacion")

        print("z calculada : ")
        print(z)
        print("z critica :")
        print(zval)


        print(i)
        conn.execute(f"INSERT INTO Z_TEST (ID,P_U1,D_U1, P_U2,D_U2,Z,P,Z_VAL,RESULTADO)\
                       VALUES ({i},'{mu1Promedios[i]}','{mu1Desv[i]}','{mu2Promedios[i]}','{mu2Desv[i]}',{z},{p},{zval},'{resultado}' )");

        # Commit your changes in the database
        conn.commit()

        # Closing the connection
    conn.close()




