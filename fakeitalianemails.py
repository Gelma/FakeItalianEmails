#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fakeitalianemails.py creates *real* fake italian email addresses

Usage: fakeitalianemails.py [OPTIONS]
OPTIONS are:
    -d, --domain   specify domain name to use (you can submit more domains separeted by space)
    -n, --number   specify how many addresses to create
    -w, --web      output as HTML comment

    Example: fakeitalianemails.py -n 5 -d 'example.com lugbs.linux.it'"

------

   Copyright 2011-2012 - Andrea Gelmini (andrea.gelmini@gelma.net)

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
"""

import copy, datetime, random, sys

class OmenNomen:
	"""Torno indirizzi nomi/cognomi/email a cazzo"""

	cognomi_elenco = [riga.strip() for riga in open(sys.path[0]+'/elenco_cognomi.txt','r')]
	nomi_elenco = [riga.strip() for riga in open(sys.path[0]+'/elenco_nomi.txt', 'r')]
	separatori = ['.', '_', '-', '']

	def __init__(self):
		self.nomi = copy.copy(self.nomi_elenco)
		self.cognomi = copy.copy(self.cognomi_elenco)
		dadi = random.SystemRandom()
		dadi.shuffle(self.nomi)
		dadi.shuffle(self.cognomi)

	def nome(self):
		"""Torno un nome a cazzo"""
		try: # se fallisco, probabilmente ho esaurito il pool di nomi
			nome_da_tornare = self.nomi[0]
		except:
			self.__init__()
			nome_da_tornare = self.nomi[0]
		self.nomi = self.nomi[1:]
		return nome_da_tornare

	def cognome(self):
		"""Torno un cognome a cazzo"""
		try: # se fallisco, probabilmente ho esaurito il pool di cognomi
			cognome_da_tornare = self.cognomi[0]
		except:
			self.__init__()
			cognome_da_tornare = self.cognomi[0]
		self.cognomi = self.cognomi[1:]
		return cognome_da_tornare

	def email(self, dominio=False, web=False, separatore=False, ordine=False, maiuscole=False, numero_finale=False):
		"""Dammi un dominio, ti torno una email a cazzo"""

		if not dominio: # se non è definito un dominio
			dominio = 'example.com'
		else:
			if ' ' in dominio: # se ho più domini, ne scelgo uno a caso
				dominio = random.choice(dominio.split())

		if web is True:
			web_testa = "<!-- "
			web_coda  = " -->"
		else:
			web_testa = web_coda = ""

		if not separatore: # scelgo un separatore a caso
			separatore = random.choice(self.separatori)

		if not ordine: # scelgo un ordine a caso per nome e cognome # ToDo: riscrivere in forma più elegante e compatta
			if random.randrange(2):
				primo_elemento, secondo_elemento = self.nome(), self.cognome()
			else:
				primo_elemento, secondo_elemento = self.cognome(), self.nome()
		elif ordine == 'n-c': # ordino per nome e cognome
			primo_elemento, secondo_elemento = self.nome(), self.cognome()
		else:
			primo_elemento, secondo_elemento = self.cognome(), self.nome()

		if not maiuscole: # ToDo: gestione con argomenti, ora faccio solo la scelta casuale
			if random.randrange(2): # decido se mettere la maiuscola oppure no
				if random.randrange(2): # se lo faccio, quale campo?
					primo_elemento = primo_elemento[0].capitalize() + primo_elemento[1:]
				else:
					secondo_elemento = secondo_elemento[0].capitalize() + secondo_elemento[1:]

		if not numero_finale: # scelgo un numero in coda (anno o incrementale)
				percentuale = random.randrange(100)
				if percentuale < 20: # metto anno di nascita
						anno_corrente = datetime.datetime.now().year
						numero_finale = str(anno_corrente - random.randrange(48))
						if percentuale < 10: # metto numero a caso
							numero_finale = str(random.randrange(70))
						numero_finale = random.choice(self.separatori)+numero_finale
				else: numero_finale=''

		return "%s%s%s%s%s@%s%s" % (web_testa, primo_elemento, separatore, secondo_elemento, numero_finale, dominio, web_coda)

if __name__ == "__main__":
	import getopt

	emails_to_create = 1	# Without arguments I use these defaults values:
	domain_to_use = False
	web = False

	try: # parsing command line arguments
		opts, args = getopt.getopt(sys.argv[1:], "hd:n:w", ["help", "domain=", "number=", "web"])
	except getopt.GetoptError, err:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(__doc__)
	for o, a in opts:
		if o in ("-h", "--help"):
			sys.exit(__doc__)
		elif o in ("-d", "--domain"):
			domain_to_use = a
		elif o in ("-n", "--number"):
			try:
				emails_to_create = int(a)
				assert emails_to_create > 0
			except:
				print "Error: number must be a *positive number*"
				print "Try 'fakeitalianemails.py --help' for more information."
				sys.exit(2)
		elif o in ("-w", "--web"):
			web = True

	email_creator = OmenNomen()
	for number in range(emails_to_create):
		print email_creator.email(dominio=domain_to_use, web=web)
