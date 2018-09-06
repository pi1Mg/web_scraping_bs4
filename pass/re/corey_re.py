import re


def file_read():
    file = open('Epictetus - The Enchiridion.txt')
    data = "r'" + file.read() + "'"
    # data = file.read()
    file.close()
    return data


pattern = re.compile(r'\bEpictetus')
matches = pattern.finditer(file_read())

for i, match in enumerate(matches):
    print(i, match)

# print(file_read()[40857:40862])
regex_b = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
# print(regex_b.match('555.555.5556'))

regex_mr = re.compile(r'M(r|s|rs)\.\s[A-Z]\w+')
#  alternative -> (Mr|Ms|Mrs)
#  alternative -> [A-Za-z]+
# print([value for value in regex_mr.finditer(file_read())])

#  get pattern for e-mail
regex_email = re.compile(r'(\w+\.?-?\w+)+@(\w+-?\w+)(\.[a-zA-Z]{2,3})+')
#  TODO: how to match ONLY domains with or 3 letters, greedy: off
# print([value for value in regex_email.finditer(file_read())])
# print([value for value in regex_email.finditer(file_read())].__len__())

#  get pattern for domains and using groups
#  TODO: figure out how not to get greedy results -> nasa.govna.us -> .gov
regex_domain = re.compile(r'https?://(www\.)?(\w+)(\.(\w{2,3}))+')
matches_domain = regex_domain.finditer(file_read())
for match in matches_domain:
    print(match.group(0))

#  re module has a method for substitution
regex_domain_sub = re.compile(r'https?://(www\.)?(\w+)(\.(\w{2,3}))+')
subbed_urls = regex_domain_sub.sub(r'\2\3', file_read())
# print(subbed_urls)

#  findall method instead of: finditer() and match()
#  findall() -> returns list of strings (if groups exist -> [(,,),(,)(,)]
print(regex_domain.findall(file_read()))

#  match() -> only returns if found at beginning of a string, else None

#  search() -> go through entire string, like match returns only 1 result
print(regex_domain.search(file_read()))

#  Flags: there are many (multi line ^ $)... Only one will be covered:
#  IGNORECASE -> if i need to find all possible combinations of upper and
#  lower letters. Short: re.I;
regex_ignore_case = re.compile(r'the', re.IGNORECASE)
print([value for value in regex_ignore_case.findall(file_read())].__len__())
















