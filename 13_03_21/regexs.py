import re
string = 'Is \^-123T ^&his \ is 3633 a test1! string 123.'

print('123' in string)
print(string.find('123'))
print(string.index('123'))

print(re.search('123', string))
print(re.search('127', string))

if re.search('127', string):
    pass

# []
# 1[0-9]7
print(re.search('[0-9][0-9][0-9]', string))
print(re.search('[h-x0-9]', string))
print(re.search('[$&(][a-b]', string))

# ^
print(re.search('[^0-9][^0-9][^0-9]', string))

# \w = [a-zA-Z0-9_]

print(re.search('\w[1-9][!@#]', string))
print(re.search('[a-zA-Z0-9_][1-9][!@#]', string))

# \W = [^a-zA-Z0-9_]

print(re.search('\W\W', string))

# \d = [0-9] \D = [^0-9]

print(re.search('\d\d', string))
print(re.search('\D\D', string))
print(re.search('[abc^]', string))

# \b  \B

print(re.search(r'\babc', '.abctext'))
print(re.search(r'abc\b', '.abc*text'))
print(re.search(r'abc\b', '.abc *text'))

# [a-zA-Z0-9_]
print(re.search('[\^a\-b\[c]', string))
print(re.search(r'[\^a\-b\[c\\]', string))

# .
print(re.search('...[a-z]', string))
# *
string_2 = '<> <tag_1> <tag_2> text </tag_2> </tag_1> '
print(re.search('<.*>', string_2))
print(re.search('<.*?>', string_2))

# +
print(re.search('<.+?>', string_2))

# \s [\t\n\r ] \S ^\s

print(re.search('<\S+?>', string_2))

# {}

print(re.search('[^0-9]{3}', string))
print(re.search('[0-9]{3,5}', '12345 jk'))
print(re.search('[0-9]{3,5}?', '12345 jk'))
print(re.search('-?[\w\s]+\.', '- String . Text'))
print(re.search('-?[\w\s]{3,}\.', 'Abc. - String . Text'))

# |
print(re.search('\d{3}|\w{3}', '!# 12567 abc 123'))

# (?=regex)regex_2
print(re.search('\w+(?=\s)', string))
# (?<=regex)regex_2
print(re.search('(?<=\s)?\w+(?=\s)?', string))
print(re.findall('(?<=\s)\w+(?=\s)', string))
print(list(re.finditer('(?<=\s)\w+(?=\s)', string)))

match_instance = re.search('(?<=\s)?\w+(?=\s)?', string)
print(match_instance.group(0))

# ()

matched_1 = re.search('(\d[a-zA-Z])*', '1b3Ux fwef')
print(matched_1.group(1))

# ^ $

print(re.search('^-?\w', '&*^String '))
print(re.search('-?\w$', '&*^String -a.'))

# print(re.search('[\da-zA-Z]*', '123h24 LA, CA, USA'))
matched_2 = re.sub('[\d]+[a-z]?', '' ,'123h24 LA, CA, USA')
print(matched_2)

multistring ="""Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used."""


print(re.findall('\w\.$', multistring, flags=re.MULTILINE))
print(*re.findall('.+?\.', multistring, re.DOTALL), sep='\n --- \n')


















