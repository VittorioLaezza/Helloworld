import math 
print("dammi in input i due coefficienti")
a=input("A:")
a=int(a)
b=input("B:")
b=int(b)

if a==0 and b==0:
	print("l'equazione è indeterminata")
elif a==0:
	print("è impossibile")
else: 
	ris=b/a

	print("la formula risolutiva è b fratto a e il risultato è",ris)
