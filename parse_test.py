#!/usr/bin/python
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

import re
import unittest
import parse


tests = ((
	"""
	==English==

	{{rank|allow|spent|soldiers|877|speech|fast|middle|effort}}

	===Etymology===
	{{etyl|ang}} ''[[spræc]]'' (later: ''spæc'')

	===Pronunciation===
	* {{IPA|/ˈspiːtʃ/}}, {{SAMPA|/"spi:tS/}}
	* {{audio|en-us-speech.ogg|Audio (US)}}
	* {{rhymes|iːtʃ}}

	===Noun===
	{{wikipedia}}
	{{en-noun|es|-}}

	# {{uncountable}} The faculty of speech; the ability to [[speak]] or to use [[vocalizations]] to [[communicate]].
	#: ''It was hard to hear the sounds of his '''speech''' over the noise.''
	# {{countable}} A session of [[speak]]ing; a long oral message given publicly usually by one person.
	#: ''The candidate made some ambitious promises in his campaign '''speech'''.''

	====Translations====
	{{trans-top|vocal communication}}
	* Armenian: {{t|hy|խոսք|sc=Armn|tr=xosk'}}
	""", 'ˈspiːtʃ'),

	("""
	{{wikisource1911Enc|Abdomen}}
	[[Image:ABDOMEN (PSF).png|thumb|right|Diagram showing the abdomen of an insect.]]
	==English==

	===Etymology===
	Latin ''abdomen'', of uncertain origin; compare French ''abdomen''

	===Pronunciation===
	* {{a|RP}} {{IPA| /ˈæbdəmən/}}
	* {{audio|en-us-abdomen.ogg|Audio (US)}}

	*: {{rhymes|əʊmən}}

	===Noun===
	{{en-noun}}

	# The [[belly]], or that part of the body between the [[thorax]] and the [[pelvis]].
	# {{anatomy}} The cavity of the belly, which is lined by the [[peritoneum]], and contains the stomach, [[bowels]], and other [[viscera]]; often restricted in humans to the part between the [
	""", 'ˈæbdəmən'),

	("""{{also|quint-}}
	==English==

	===Pronunciation===
	* ''(A musical or piquet term, or a quintuplet)'' {{IPA|/kwɪnt/}}
	* ''(A fencing term)'' {{IPA|/kwɛ̃/}}

	===Noun===
	{{wikipedia}}
	{{en-noun}}

	# {{music}} an [[interval]] of one [[fifth]]
	# (''in piquet'') a [[sequence]] of five [[playing card]]s of the same [[suit]]; equivalent to a [[straight flush]] in poker
	# {{US}} a [[quin]] or [[quintuplet]]
	# [[quinte]]; In fencing, the fifth fencer in parrying or attacking position.

	----

	==Catalan==
	{{ordinalbox|ca|4t|5t|6t|quart|sext|card=cinc|mult=quíntuple}}

	===Etymology===
	From {{etyl|la|ca}} {{term|lang=la|quintus||fifth}}

	===Ordinal number===
	{{ca-num-ord}}
	# {{ordinal|lang=ca}} [[fifth]]
	""", "kwɪnt"),
)


for (i, (str_input, exp_output)) in enumerate(tests):
	input = re.compile(r'^\s*', re.M).sub('', str_input) # trim whitespace
	locals()['foo' + str(i)] = type(
		'foo' + str(i),
		(unittest.TestCase,),
		{
			'input': input,
			'exp_result': exp_output,
			'errstr': u"failed to match in %s" % i,
			'testme': lambda self: self.assertEqual(parse.parse_ipa(self.input)[0], self.exp_result) #, self.errstr.encode('utf8'))
		})


if __name__ == '__main__':
	unittest.main()
