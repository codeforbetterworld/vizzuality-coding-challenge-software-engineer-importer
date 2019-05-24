import sys
sys.path.append("..")
from dataFormatter import csvDataFormatter

def getCsvRows(csvFile):
    csvData = []
    for line in csvFile:
        csvData.append(csvDataFormatter.formatLine(line))
    return csvData

def getCsvColumns(csvData):
    return csvData[0]