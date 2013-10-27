# -*- coding: utf-8 -*-
from random import shuffle

def chooseRandomCard(cards):
	"""Wält eine zufällige Karte aus dem Dictionary cards aus und 
	gibt den key und value als tupel (key, value) zurück"""
	keys = cards.keys()
	shuffle(keys)
	return (keys[0], cards[keys[0]])

def unicodeInput(prompt):
	"""Input mit Umlauten"""
	return unicode(raw_input(prompt.encode('utf-8')), 'utf-8')

# Für Umlaute:
# - alle Strings mit einem u vor den Anfürungszeichen versehen z.B. u"Inhal..."
# - statt input die Funktion unicodeInput verwenden
start = False
karten = {}
while not start:
	vorderseite = unicodeInput(u"Bitte Vorderseite eingeben: ")
	rueckseite = unicodeInput(u"Bitte Rückseite eingeben: ")
	karten[vorderseite] = rueckseite
	start = (unicodeInput(u"Mit dem Abfragen beginnen? (j/n): ") == "j")
karten = {u'to watch': u'schauen', u'to sit': u'sitzen', u'to eat': u'essen', u'to laugh': u'lachen', u'to drink': u'trinken', u'to swim': u'schwimmen', u'to wrtie': u'schreiben'}
while karten:
	card = chooseRandomCard(karten)
	if card[1] == unicodeInput(u"%s?: " % (card[0])):
		print u"Richtig! :) %s - %s" % card
		del karten[card[0]]
	else:
		print u"Leider falsch! Das wär's gewesen: %s - %s" % card