import re

words=[
    "orange","october","octpus",
    "order","banana","baby","busy"
]

pattern = r"oc.*"
print("ocで始まるパターン=",pattern)
for word in words:
    if re.match(pattern,word):
        print("-",word)

pattern = r"b.*y"
print("bで始まり,yで終わるパターン=",pattern)
for word in words:
    if re.match(pattern,word):
        print("-",word)
