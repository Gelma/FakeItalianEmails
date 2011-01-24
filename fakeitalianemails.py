#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy, random, sys

class OmenNomen:
	"""Torno indirizzi nomi/cognomi/email a cazzo"""

	cognomi_elenco = [riga.strip() for riga in open(sys.path[0]+'elenco_cognomi.txt','r')]
	nomi_elenco = [riga.strip() for riga in open(sys.path[0]+'elenco_nomi.txt', 'r')]

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
