#replaceletter
string = 'The quick brown fox jusmps over the lazy dog'
# Define your variables
result = ''
for i in string:
        if i == 'o':
                i = '0'
        result += i
print (result)

a="alan"
ch="a"
c=a.replace(ch,"")
print(c)
