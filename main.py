import re

pattern = re.compile('this')
pattern_3 = re.compile('search inside of this this text')
string = 'search inside of this this text, please.'

result = pattern.search(string)
result_2 = pattern.findall(string)
result_3 = pattern_3.fullmatch(string)
result_4 = pattern_3.match(string)

print(result)#<re.Match object; span=(17, 21), match='this'>

print(result.group())#this

print(result_2)#['this', 'this']]

print(result_3)#<re.Match object; span=(0, 31), match='search inside of this this text'> OR #None

print(result_4)#<re.Match object; span=(0, 31), match='search inside of this this text'>
