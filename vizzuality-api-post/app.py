from flask import Flask, request
from infrastructure import mongodbPersist
from dataRetriever import getCsvData
from dataFormatter import emissionsDataFormatter

app = Flask(__name__)

@app.route("/emissions", methods = ['POST'])
def emissions():
    csvFile = request.files['file']
    csvData = getCsvData.getCsvRows(csvFile)
    csvColumns = getCsvData.getCsvColumns(csvData)
    dataFormattedTopersist = emissionsDataFormatter.formatData(csvColumns,csvData)
    mongodbPersist.save(dataFormattedTopersist)
    return 'File imported successfully'