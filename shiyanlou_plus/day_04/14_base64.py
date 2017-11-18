import base64

encode = base64.b64encode(b"Hello, shiyanlou!")
print("encode \'Hello, shiyanlou!\': {0}".format(encode))

decode = base64.b64decode(encode)
print("decode for var \'encode\': {0}".format(decode))
