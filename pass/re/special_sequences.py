import re


#  Special sequences

#  .        -- matches any character except new ine
regex_dot = re.compile(r'\.')

#  \d       -- matches any decimal digit - [0-9]
regex_d = re.compile(r'\d')

#  \D       -- matches any non-digit character - [^0-9]
regex_D = re.compile(r'\D')

#  \s       -- matches any whitespace character (space, tab, new line)
regex_s = re.compile(r'\s')

#  \S       -- matches any non-whitespace character
regex_S = re.compile(r'\S')

#  \w       -- matches any alphanumeric character - [a-zA-Z0-9_]
regex_w = re.compile(r'\w')

#  \W       -- matches any non-alphanumerical character - [^a-zA-Z0-9_]
regex_W = re.compile(r'\W')

#  ANCHORS
#  \b       -- word boundary - gives me an index of before boundary(Ha HaHa)
regex_b = re.compile(r'\bHa')
print([reg for reg in (regex_b.finditer('Some Ha HaHa end.'))])
# [<_sre.SRE_Match object; span=(5, 7), match='Ha'>, <_sre.SRE_Match object; span=(8, 10), match='Ha'>]

#  \B       -- not a word boundary
regex_B = re.compile(r'\BHa')
print([reg for reg in (regex_b.finditer('Some Ha HaHa end.'))])
# [<_sre.SRE_Match object; span=(10, 12), match='Ha'>]







