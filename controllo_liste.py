#!/usr/bin/env python
"""Voglio un file o un stdin come argomento,
segnalo tutte le righe che contengano
caratteri non validi per la nostra generazione di
nomi.
"""

import fileinput, re

valid_email_chars = re.compile('[a-z0-9_-]+$')

for line_number, line in enumerate(fileinput.input()):
	if not valid_email_chars.match(line):
		print "Error %s: %s" % (line_number+1, line.strip())
