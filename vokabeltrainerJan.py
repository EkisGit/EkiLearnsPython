# -*- coding: utf-8 -*-

from random import shuffle
def chooseRandomCard(cards):
	keys = cards.keys()
	shuffle(keys)
	return (keys[0], cards[keys[0]])

def unicodeInput(prompt):
	return unicode(raw_input(prompt.encode('utf-8')), 'utf-8')


start = False
vocabluary = {}
while not start:
	front = unicodeInput(u"Bitte Vorderseite eingeben: ")
	back = unicodeInput(u"Bitte Rückseite eingeben: ")
	vocabluary[front] = back
	start = (unicodeInput(u"Mit dem Abfragen beginnen? (y/n): ") == "y")
while vocabluary:
	card = chooseRandomCard(vocabluary)
	if card[1] == unicodeInput(u"%s?: " % (card[0])):
		print u"Richtig: %s - %s" % card
		del vocabluary[card[0]]
	else:
		print u"Später nochmal... Richtig wäre: %s - %s" % card