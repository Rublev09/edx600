def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    def findspace(text,lineLength):
        if len(text) <= lineLength or ' ' == text[lineLength-1]:
            return lineLength
        return 1 + findspace(text[1:], lineLength) 
    if len(text) ==0:
        return ''
    newline = text[:findspace(text,lineLength)] 
    newtext = text[findspace(text,lineLength):]
    return newline + "\n" +insertNewlines(newtext, lineLength)

print insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)
