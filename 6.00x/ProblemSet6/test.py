import string
text = "what the heck it's friday afternoon!"
punct = list(string.punctuation)

textlist = list(text.lower())

for n, i in enumerate(textlist):
    if i in punct:
        textlist[n] = ' '

newtext = ''.join(textlist)
newlist = newtext.split()




