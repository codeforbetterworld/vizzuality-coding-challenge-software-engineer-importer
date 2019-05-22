def getCsvRows(csvFile):
    csvData = []
    for line in csvFile:
        csvData.append(line.decode('utf-8').replace('\r\n', '').split(','))
    return csvData

def getCsvColumns(csvData):
    return csvData[0]