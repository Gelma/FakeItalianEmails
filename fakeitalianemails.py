#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy, random, sys

class OmenNomen:
	"""Torno indirizzi nomi/cognomi/email a cazzo"""

	cognomi_elenco = [riga.strip() for riga in open(sys.path[0]+'/elenco_cognomi.txt','r')]
	nomi_elenco = [riga.strip() for riga in open(sys.path[0]+'/elenco_nomi.txt', 'r')]

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

	def email(self,dominio):
		"""Dammi un dominio, ti torno una email a cazzo"""
		return self.nome()+'_'+self.cognome()+'@'+dominio

if __name__ == "__main__":
	import getopt

	emails_to_create = 1	#Without arguments I use these defaults values:
	domain_to_use = 'example.com'

	try: # parsing command line arguments
		opts, args = getopt.getopt(sys.argv[1:], "hd:n:", ["help", "domain=", "number="])
	except getopt.GetoptError, err:
		print str(err) # will print something like "option -a not recognized"
		print "Try 'fakeitalianemails.py --help for more information."
		sys.exit(2)
	for o, a in opts:
		if o in ("-h", "--help"):
			print "fakeitalianemails.py creates *real* fake italian email addresses"
			print "Usage: fakeitalianemails.py [OPTIONS]\n\nOPTIONS are:\n\t-d, --domain\t specify domain name to use\n\t-n, --number\t specify how many addresses to create\n"
			sys.exit()
		elif o in ("-d", "--domain"):
			domain_to_use = a
		elif o in ("-n", "--number"):
			try:
				emails_to_create = int(a)
				assert emails_to_create > 0
			except:
				print "Error: number must be a *positive number*"
				print "Try 'fakeitalianemails.py --help for more information."
				sys.exit(2)

	email_creator = OmenNomen()
	for number in range(emails_to_create):
		print email_creator.email(domain_to_use)
