import re # importing regular expression classes
text_to_search='abcidehfkjfergtrumabbbbbbbabc'

pattern=re.compile(r'abc')
pattern1=re.compile(r'abc\.') # this will escape to the dot and we can put any pattern here



matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)

# print(text_to_search[1:4])