import sys

import MySQLdb

db = MySQLdb.connect(user='nick', db='wikipedia')

c = db.cursor()

print "type the number equivalent to this word"

try:
	while 1:
		c.execute("select number, word from pro order by rand() limit 1")
		
		(number, word) = c.fetchone()

		print word, '?'
		

		while 1:
			input = sys.stdin.readline()

			if not input.strip():
				print "correct was", number
				print
				break

			try:
				if int(input.strip()) == int(number):
					print "correct"
					print
					break
				else:
					raise ValueError

			except ValueError:
				print "incorrect, try again"


except (SystemExit, KeyboardInterrupt):
	print "exiting..."
	raise SystemExit
