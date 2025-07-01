# si.py
#Simple Interest


P=float(input("muldhan dalo: ") )
R=float(input("Enter rate of interest: ") )
T=float(input("time dalo: ") )
#P*T*I/100
#PRT/100

#SI=(P*R*T)/100
SI=P*R*T
SI /=100
print(f"Simple Interest Is {SI}.")