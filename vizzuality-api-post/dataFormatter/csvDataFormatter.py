def formatLine(line):
    formattedLine = setEncodingUtf8(line)
    formattedLine = removeNewLineCharactersRN(formattedLine)
    formattedLine = splitLineCommaSeparated(formattedLine)
    return formattedLine

def setEncodingUtf8(line):
    return line.decode('utf-8')

def removeNewLineCharactersRN(line):
    return line.replace('\r\n', '')

def splitLineCommaSeparated(line):
    return line.split(',')