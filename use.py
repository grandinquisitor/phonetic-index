import sys

import MySQLdb

db = MySQLdb.connect(user='nick', db='wikipedia')

c = db.cursor()


print "how may i help you?"
print "1) look up a word for a number"
print "2) look up a number for a word"


try:

	choice = sys.stdin.readline().strip()


	if choice == '1':
		while True:
			print "number:"
			number = sys.stdin.readline().strip()
			try:
				int(number)
			except ValueError:
				print "that's not a number, is it?"
			else:
				num_found = c.execute("select word from pro where number=%s", number)

				print "found", num_found, ", ".join(x[0] for x in c.fetchall())


	elif choice == '2':
		while True:
			print "word:"
			word = sys.stdin.readline().strip()

			num_found = c.execute("select number from pro where word=%s", word)

			if not num_found:
				print "none found"
			else:
				print c.fetchone()[0]


	else:
		print "unknown choice"

except KeyboardInterrupt:
	print "exiting"
