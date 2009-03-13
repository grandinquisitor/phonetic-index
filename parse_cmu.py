
import re

#alternative idea:
# map these to IPA chars
include = {
	'B': 9,
	'CH': 6,
	'D': 1,
	'DH': 1,
	'ER': 4,
	'F': 8,
	'G': 7,
	'JH': 6,
	'K': 7,
	'L': 5,
	'M': 3,
	'N': 2,
	'P': 9,
	'R': 4,
	'S': 0,
	'SH': 6,
	'T': 1,
	'TH': 1,
	'V': 8,
	'Z': 0,
	'ZH': 6
}

exclude = set(('NG',))

f = open('cmudict.0.7a.cut', 'r')

for line in f.readlines():
	(_, word, pron) = re.compile(r'^(\S+)\s+').split(line[0:-1])
	syl = pron.split(' ')
	
	if not re.compile(r'\(\d+\)$').search(word) \
			and not any(p for p in  syl if p in exclude):

		try:
			parts = [include[p] for p in (p if p[-1] not in ('0', '1', '2') else p[:-1] for p in syl) if p in include]
		except IndexError:
			continue

		if parts:
			print re.compile(r'(?<=\b\')[A-Z]').sub(lambda x: x.group().lower(), word.title()) + '|' + ''.join(map(str, parts))

