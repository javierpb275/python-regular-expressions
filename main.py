import re

pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search inside of this text, please.'

result = pattern.search((string))

print(result.group())#sea
