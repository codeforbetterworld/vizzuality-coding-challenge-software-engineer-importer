import os

eget = os.environ.get

CHARACTER_ENCODING=eget('CHARACTER_ENCODING')
CSV_NEWLINE_CHARACTERS=eget('CSV_NEWLINE_CHARACTERS')
CSV_SEPARATOR=eget('CSV_SEPARATOR')

def formatLine(line):
    formattedLine = setEncoding(line)
    formattedLine = removeNewLineCharacters(formattedLine)
    formattedLine = splitLine(formattedLine)
    return formattedLine

def setEncoding(line):
    return line.decode(str(CHARACTER_ENCODING))

def removeNewLineCharacters(line):
    return line.replace(str(CSV_NEWLINE_CHARACTERS), '')

def splitLine(line):
    return line.split(str(CSV_SEPARATOR))