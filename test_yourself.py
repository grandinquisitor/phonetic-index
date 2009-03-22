import sys
import random

import MySQLdb

db = MySQLdb.connect(user='nick', db='wikipedia')

c = db.cursor()

try:

	print "game type?"

	choice = sys.stdin.readline().strip()

	if choice == '1':
		print "what number is this word?"
		print

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

	elif choice == '2':

		while 1:
			num = str(random.randint(0, 999))

			c.execute("select count(*) from pro where number=%s", num)

			if c.fetchone()[0] == 0:
				continue


			print "pick a word for this number:", num

			while 1:
				input = sys.stdin.readline().strip()

				if not input:
					c.execute("select word from pro where number=%s", num)
					print 'correct could have been:', ', '.join(x[0] for x in c.fetchall())
					break

				c.execute("select count(*) from pro where word=%s and number=%s", (input, num))

				cnt = c.fetchone()[0]

				if cnt:
					print "correct"
					print
					break
				else:
					print "incorrect, try again"

		
	else:
		print "unknown game type"
		print


except (SystemExit, KeyboardInterrupt):
	print "exiting..."
