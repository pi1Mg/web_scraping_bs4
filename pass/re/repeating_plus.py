import re


#  + character -- this specifies that previous character
#  can be matched one or more times
#  diff from asterisk ('a*') -> 0 to inf; + -> 1 to inf
regex_plus = re.compile('a+')
print(regex_plus.match('aaaaa'))
# <_sre.SRE_Match object; span=(0, 5), match='aaaaa'>
print(regex_plus.match(''))
# None

#  Using character classes
regex_char_class_plus = re.compile('[a-c]+')
print(regex_char_class_plus.match('abcabcabc'))
# <_sre.SRE_Match object; span=(0, 9), match='abcabcabc'>
print(regex_char_class_plus.match(''))
# None
#  Asterisk would return 0, plus returns None



