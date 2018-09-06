import re


#  re.compile       -- returns a regex object
#  pattern that we want to find
regex = re.compile('[^a-zA-Z]')

#  regex.match(string_to_match)
#  -- returns None if no match else returns a match object
#  string in which we want to find a pattern via match method
print(regex.match('1'))



