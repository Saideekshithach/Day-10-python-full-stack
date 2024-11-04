Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={"idnos":[10,20,30],"names":["manikanta","rajesh","yogeshwar"]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['manikanta', 'rajesh', 'yogeshwar']}
>>> type(a)
<class 'dict'>
>>> a={"idnos":10,20,30,"names":"manikanta","rajesh","yogeshwar"}
SyntaxError: ':' expected after dictionary key
