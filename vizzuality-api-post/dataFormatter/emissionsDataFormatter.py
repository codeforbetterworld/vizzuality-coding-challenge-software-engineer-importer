def formatData(csvColumns, csvData):
    data = {}
    insertionUnit = {}
    allData = []
    for j in range(1,len(csvData)):
        for i in range(len(csvColumns)):
            data = { str(csvColumns[i]) : str(csvData[j][i]) }
            insertionUnit.update(data)
            data.clear()
        allData.append(insertionUnit.copy())
        insertionUnit.clear()
    return allData