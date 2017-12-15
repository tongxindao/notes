try:
    raise UnicodeDecodeError("pdfdocencoding", "a",2, -1, "not support decoding")
except ValueError: # python2 show this
    print("ValueError Occured")
except UnicodeDecodeError as e: # python3 show this
    print(e)
