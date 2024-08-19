"""
f = open("multipalLines.txt")

data = f.readlines()
print(data)

# ['Hey My name is Gaurav.\n', 'I am a very Good boy.\n', 'This is Third Line.\n', 'This is fourth Line.\n', '\n', '\n', '\n']

print(type(data)) # <class 'list'>

f.close()

"""

# printing line by line

f = open("multipalLines.txt")
line = f.readline()

while(line != "" ):
    if(line == "\n"):
        break
    print(line)
    line = f.readline()

f.close()

# Its print only text line not the empty line
# printing all line at once
"""
Hey My name is Gaurav.

I am a very Good boy.

This is Third Line.

This is fourth Line.

"""

