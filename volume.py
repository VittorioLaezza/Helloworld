import math
print("calcola volume di un cubo o di una sfera")
print("effettua scelta 1=volume-2=sfera")
lato=input("lato")
lato=int(lato)
raggio=input("raggio")
raggio=int(raggio)
scelta=input("1-2 ")
scelta=int(scelta)

if scelta==1:
	
	cubo=lato*lato*lato
	print("il cubo di",lato," e'",cubo)
elif scelta==2:
	
	volume= 4/3 * math.pi *raggio*raggio*raggio
	print("il volume di",raggio," e'",volume)
else:
	print("premi 1 o 2")