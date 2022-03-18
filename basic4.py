#1
# n = int(input())
# res = []
# for i in range(0, n):
#     a, b = map(str, input().split())
#     res.append([a, b])

# for i in res:
#     try:
#         print (str(int(i[0]) // int(i[1])))
#     except ZeroDivisionError as e:
#         print ("Error Code:", e)
#     except ValueError as e:
#         print("Error Code:", e)

# 2

# import re
# n = int(input())
# arr = []
# for i in range(0, n):
#     string = input()
#     arr.append(string)

# res = []
# for i in arr:
#     x = re.findall("^102[12][78901][0][0123456789]\d{2}$", i)
#     res.append(x)

# for i in res:
#     if len(i) > 9:
#         print("False")
#     else:
#         if i:
#             print("True")
#         else:
#             print("False")

# 3
# import re
# n = input()
# pat = r'(?<=\<).+?(?=\>)'
# match = re.findall(pat, n)
# print(match)

#4
# import re
# n = input()
# m = input()
# subs = [m]
# res = re.findall(r'({0})\s*(.*?)(?=\s*(?:{0}|$))'.format("|".join(subs)), n)
# print(len(res[0]))

#5

# import re
# n = int(input())
# arr = []
# for i in range(0, n):
#     pattern = input()
#     arr.append(pattern)
# for i in arr:
#     try:
#         re.compile(i)
#         print("True")
#     except re.error:
#         print("False")

# 6

# import re
# n = input()
# target = n.replace('.', '-')
# result = re.split(r"-|,", target)
# for i in result:
#     print(i)

#7

# import re
# n = int(input())
# arr = []
# res = []
# for i in range(0, n):
#     a = input()
#     arr.append(a)

# regex = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'

# def check(regex, email):
#     if len(email.split(".")) > 1:
#         if len(email.split(".")[1]) > 3:
#             return False
#         else:
#             if(re.fullmatch(regex, email)):
#                 return True
#             else:
#                 return False
#     else:
#         return False

# for i in arr:
#     if check(regex, i):
#         res.append(i)

# res.sort()
# print(res)

#8
# import re
# import itertools
# n = int(input())
# arr = []
# for i in range(0, n):
#     a = input()
#     arr.append(a)

# def check(text):
#     l=[(k, sum(1 for i in g)) for k,g in itertools.groupby(text)]
#     if re.search(r'^[456]+',text) and len(text)==16  and re.search(r'[\d]',text) and all(v<=3 for k,v in l) and bool(re.search(r'\s',text)) is False and bool(re.search(r'[a-z]',text)) is False or( bool(re.search(r'-',text))is True and len(text)==19) :
#         return True

#     else :
#         return False

# for i in arr:
#     if check(i):
#         print("True")
#     else:
#         print("False")

# import re
# n = int(input())
# arr = []
# for i in range(0, n):
#     text = input()
#     arr.append(text)
# for text in arr:
#         try:
#             assert re.fullmatch(r'[456]\d{3}(-|)\d{4}(-|)\d{4}(-|)\d{4}',text)
#             assert not(re.search(r'(\d)\1{3,}',text.replace("-","")))
        
#         except AssertionError:
#             print('False')
#         else:
#             print('True')


import re
text = input()
text1 = input()
regex = '(?=' + text1 + ')'
print(len(re.findall(regex, text)))