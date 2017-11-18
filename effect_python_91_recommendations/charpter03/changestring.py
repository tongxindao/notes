import array

teststr = "I am a python string"
change = array.array("u", teststr)
print("Before Change: " + change.tounicode())
print("=" * 40)
change[10] = "H"
print("After Change: " + change.tounicode())
