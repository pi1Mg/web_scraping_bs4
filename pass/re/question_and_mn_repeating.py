import re


#  ? question mark -- previous character can either come once or not at all
#  0 or 1; min 0, max 1;
regex_question = re.compile('a?b')
print(regex_question.match('b'))
# <_sre.SRE_Match object; span=(0, 1), match='b'>
print(regex_question.match('ab'))
# <_sre.SRE_Match object; span=(0, 2), match='ab'>
print(regex_question.match('aaaab'))
# None
print(regex_question.match(''))

#  {m,n}    m,n are int     --
#  This qualifier means: there must be at least m repetitions, and at most n
regex_custom_rep = re.compile('a{2,4}')  # aa aaa aaaa
print(regex_custom_rep.match('a'))
# None
print(regex_custom_rep.match('aaaaaaa'))
# <_sre.SRE_Match object; span=(0, 4), match='aaaa'>
print(regex_custom_rep.match('aabb'))
# <_sre.SRE_Match object; span=(0, 2), match='aa'>
print(regex_custom_rep.match('bbaa'))
# None

#  * {0,}       --  matches from zero to infinity
regex_zero_inf = re.compile('a{0,}')
print(regex_zero_inf.match('aaa'))
# <_sre.SRE_Match object; span=(0, 3), match='aaa'>

#  + {1,}

#  ? {0,1}

#  To match only specific, defined set of char, use [char1char2]
#  it will match char1 or char2 etc..
#  [89]00 will find 800s and 900s
#  [1-5] will find all from 1 to 5, [a-c] = a,b,c
#  outside ^ -> search start, inside [^] -> negates

#  Quantifiers:
#  *        - 0 or more
#  +        - 1 or more
#  ?        - 0 or 1
#  {3}      - Exact number - re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}'
#  {3,4}    - Range of numbers (min, max)







