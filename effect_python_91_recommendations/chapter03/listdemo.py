words = [' Are', ' abandon', 'Passion', 'Business', ' fruit ', 'quit']
size = len(words)

newlist = [words[i] for i in range(size) if words[i].strip().istitle()]

print(newlist)
