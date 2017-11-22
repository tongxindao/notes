import os

print("get current work diretory: {0}".format(os.getcwd()))
print("generate 24 bit random string: {0}".format(os.urandom(24)))
os.mkdir('web-app')
os.mknod(os.getcwd() + '/app.py')
