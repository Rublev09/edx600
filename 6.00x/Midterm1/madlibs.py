def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    # Your Code Here
    madform = story.split()
    for n,word in enumerate(madform):
        for adj in listOfAdjs:
            if adj == word:
                madform[n] = '[ADJ]'
        for verb in listOfVerbs:
            if verb == word:
                madform[n] = '[VERB]'
        for noun in listOfNouns:
            if noun == word:
                madform[n] = '[NOUN]'
    
    return ' '.join(madform)

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    # Your Code Here
    newlist = madLibsForm.split()
    correctorder = []
    for word in newlist:
        if word  == '[ADJ]' or word == '[VERB]' or word == '[NOUN]':
            correctorder.append(word)
    return correctorder


def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    # Your Code Here
    if madTemplate == '[ADJ]':
        return userWord in listOfAdjs
    if madTemplate == '[VERB]':
        return userWord in listOfVerbs
    if madTemplate == '[NOUN]':
        return userWord in listOfNouns
    
        
            


story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)

story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']
print generateTemplates(generateForm(story, listOfAdjs, listOfNouns, listOfVerbs))

print verifyWord('store', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs)
