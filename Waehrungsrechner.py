def euroZuDollar(euro):
	dollar = euro * 1.3541
	return dollar

def dollarZuEuro(dollar):
	euro = dollar / 1.3541
	return euro

frage = input("Was moechten Sie umrechnen? Fuer Dollar zu Euro tippen Sie 1 und fuer Euro zu Dollar 2: ")
if frage == 1 : 
	dollarEingabe = input("Geben Sie hier den Dollar-Betrag ein: ")
	euro = dollarZuEuro(dollarEingabe)
	print "Das sind %.4f Euro" % (euro)
elif frage == 2:
	euroEingabe = input("Geben Sie hier den Euro-Betrag ein: ")
	dollar = euroZuDollar(euroEingabe)
	print "Das sind %.4f$" % (dollar)


