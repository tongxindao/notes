str1 = "hello"
str2 = "shiyanlou"
str3 = "hello, \'shiyanlou\'"
str4 = "hello, 'shiyanlou'"
str5 = 'hello, "shiyanlou"'
str6 = """hello,
shiyanlou"""

print("str1 + str2 = {0}".format(str1 + ' ' + str2))
print("str1 = {0}".format(str1))
print("str1[0] is: {0}".format(str1[0]))
print("str1[1] is: {0}".format(str1[1]))
print("str1[-1] is: {0}".format(str1[-1]))
print("str1[-2] is: {0}".format(str1[-2]))
print("str1[:2] is: {0}".format(str1[:2]))
print("str1[3:] is: {0}".format(str1[3:]))
print("\'len(str2)\' result is: {0}".format(len(str2)))
