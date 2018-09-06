import re


#  ^ character      -- says that string should start with
regex_start_with = re.compile('^abc')
print(regex_start_with.match('abcda'))
# <_sre.SRE_Match object; span=(0, 3), match='abc'>

#  | character      -- is the or operator
regex_or = re.compile('a|b')
print(regex_or.match('ac'))
# <_sre.SRE_Match object; span=(0, 1), match='a'>
print(regex_or.match('ba'))
# <_sre.SRE_Match object; span=(0, 1), match='b'>

#  $ character -- matches the end of line
regex_dollar = re.compile('ab$')
print(regex_dollar.match('ab'))