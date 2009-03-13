# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

import re
from xml.dom import pulldom
import sys

import pronunciation


get_title = lambda n: n.getElementsByTagName('title')[0].childNodes[0].nodeValue

def get_text(n):
	txt = n.getElementsByTagName('text')[0]
	txt.normalize()
	return txt.childNodes[0].nodeValue


def err(*args):
	pass
	#print >>sys.stderr, ' '.join(a.encode('utf8') for a in args)


def parseit(fname):
	doc = pulldom.parse(fname)

	for event, node in doc:
		if event == pulldom.START_ELEMENT and node.localName == 'page':
			doc.expandNode(node)

			page_title = get_title(node)

			if ':' in page_title:
				err("wrong namespace", page_title)

			elif isnt_all_caps(page_title):
				err("bad page title", page_title)

			elif page_title[0] == '-' or page_title[-1] == '-':
				err("looks like a prefix or suffix", page_title)

			else:
				try:
					page_text = get_text(node)
				except IndexError:
					err("bad node", page_title.encode('utf8'))
				else:
					ipa_notes = parse_ipa(page_text)
					if not has_english_definition(page_text):
						err("not english", page_title.encode('utf8'))
					elif not ipa_notes:
						err("no pronunciation", page_title.encode('utf8'))
					else:
						try:
							(pro_keys, num_vals) = pronunciation.parse_word(ipa_notes[0])
						except ValueError, e:
							err("pron.", page_title, "not useable", ipa_notes[0].encode('utf8'), '-->', e.message.encode('utf8'))
						else:
							if num_vals:
								print page_title.encode('utf8') + '|' + ''.join(num_vals)



# {{IPA|/ˈdɪkʃən(ə)ɹi/}}

def parse_ipa(page_text):
	# must be in the english region
	page_region = re.compile(r'^==\s*English\s*==.*?(?:^==[^=]|\Z)', re.M | re.S).search(page_text)
	if page_region:
		results = re.compile(ur'{{IPA \s* \| \s* / ([^/\|]*) (?:/\|/[^/]*)? (?:\|lang=en)? /}}', re.X).findall(page_region.group())
		return results
	else:
		return []

def has_english_definition(page_text):
	return bool(re.compile('^==\s*English\s*==', re.M).search(page_text))

def isnt_all_caps(page_title):
	return not re.compile('[a-z]').search(page_title)

if __name__ == '__main__':
	try:
		parseit('enwiktionary-20090203-pages-articles.xml')
	except KeyboardInterrupt:
		pass
