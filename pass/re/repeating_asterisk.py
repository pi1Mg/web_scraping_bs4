import re


#  * character - this specifies that the previous character can be matched
#  zero or more times, instead of exactly once. Output from 0 to inf
regex_asterisk = re.compile('a*')
print(regex_asterisk.match('aaaaa'))
#  returns: <_sre.SRE_Match object; span=(0, 5), match='aaaaa'>
print(regex_asterisk.match(''))
#  returns: <_sre.SRE_Match object; span=(0, 0), match=''>

regex_asterisk_ = re.compile('[a-c]*')
print(regex_asterisk_.match('bbbb'))
#  retutns: <_sre.SRE_Match object; span=(0, 4), match='bbbb'>
print(regex_asterisk_.match('b12121bbbb'))
#  returns: <_sre.SRE_Match object; span=(0, 1), match='b'>
print(regex_asterisk_.match('baaaaaaaaaaaaaaaabccccccc'))
# returns: <_sre.SRE_Match object; span=(0, 25), match='baaaaaaaaaaaaaaaabccccccc'>

