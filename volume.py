import math
print("calcola volume di un cubo o di una sfera")
print("effettua scelta 1=volume-2=sfera")


scelta=input("1-2 ")
scelta=int(scelta)

if scelta==1:
	lato=input("lato")
	lato=int(lato)
	cubo=lato*lato*lato
	print("il cubo di",lato," e'",cubo)
elif scelta==2:
	raggio=input("raggio")
	raggio=int(raggio)
	volume= 4/3 * math.pi *raggio*raggio*raggio
	print("il volume di",raggio," e'",volume)
else:
	print("premi 1 o 2")