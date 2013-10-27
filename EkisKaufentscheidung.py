preisInEuroProdukt1 = input("Preis Produkt 1 in Euro: ")
gewichtInGrammProdukt1 = input("Gewicht Produkt 1 in Gramm: ")
preisInEuroProdukt2 = input("Preis Produkt 2 in Euro: ")
gewichtInGrammProdukt2 = input("Gewicht Produkt 2 in Gramm: ")
preis1DurchGewicht1 = 1.0 * preisInEuroProdukt1 / gewichtInGrammProdukt1
preis2DurchGewicht2 = 1.0 * preisInEuroProdukt2 / gewichtInGrammProdukt2
if preis1DurchGewicht1 < preis2DurchGewicht2 :
	print "Das erste Produkt ist billiger"
elif preis2DurchGewicht2 < preis1DurchGewicht1 :
	print "Das zweite Produkt ist billiger"
else:
	print "Die Produkte kosten gleich viel"
