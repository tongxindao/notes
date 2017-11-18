"""
This is a python test for learn by imooc class
"""


ACCOUNT = "tongxindao"
PASSWORD = "admin123"

print("Please input account")
user_account = input()

print("Please input password")
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password:
    print("Success!")
else:
    print("Fail!")
