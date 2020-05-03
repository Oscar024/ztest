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
    elif type == "ColaDerecha":
        zValue = st.norm.ppf(1 - alpha)
        if z > zValue:
            pasalaPrueba=1;
        else:
            pasalaPrueba=0;
    elif type == "DosColas":
        if z >= st.norm.ppf(alpha) and z<= st.norm.ppf(1 - alpha):
            pasalaPrueba=1;
        else:
            pasalaPrueba=0;
    else:
        print("Error tyoe")
    return pasalaPrueba,round(z, 3), round(pval, 4), round(zValue,3)


alpha=0.05;
x1=0.000155
x2=0.0084
std1=0.000041
std2=0.0395
n1=30
n2=30
type="ColaIzquierda"
#type="ColaDerecha"
#type="DosColas"

resultado,z,p, zval= twoSampZ(28, 33, 14.1, 9.5, 75, 50,0.05,type)

if resultado == 1:
    print("Hay suficiente evidencia para apoyar la afirmacion")
else:
    print("No hay suficiente evidencia para apoyar la afirmacion")

print("z calculada : ")
print(z)
print("z critica :")
print(zval)
