def gebeListeAus(liste):
	for zahl in liste:
		print zahl
	return True

eingabe = input("Geben Sie hier die ganze Zahl ein, bis zu der der Computer zaehlen soll: ")
aktuelleZahl = 0
while aktuelleZahl < eingabe:
	aktuelleZahl += 1
	print aktuelleZahl
einsBisZehn = (1,2,3,4,5,6,7,8,9,10)

gebeListeAus((3,4,5,2,5))
erfolg = gebeListeAus(einsBisZehn)
if erfolg:
	print "juhuu"
else:
	print "oh neien!"



