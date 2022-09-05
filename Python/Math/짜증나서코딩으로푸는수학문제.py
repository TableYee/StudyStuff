import math as ma
BP = 1
m = 100000
for PQ in range(5,int(ma.sqrt(3)*100),5):
    BQ = ma.sqrt(BP**2 + PQ**2)
    temp = ((ma.sqrt(3)-PQ)**2 + 2*(BQ**2))
    if temp < m:
        m = temp
        x = PQ
        
print((m/100)/x)