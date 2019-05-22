const express = require('express')
const bodyParser = require('body-parser')
const MongoClient = require('mongodb').MongoClient

const databaseName = process.env.MONGO_APP_DATABASE_NAME
const url = `mongodb://${process.env.MONGO_APP_USER}:${process.env.MONGO_APP_USER_PASSWORD}@${process.env.MONGO_HOST}/${databaseName}:27017?authMechanism=SCRAM-SHA-1&authSource=admin`
const options = {
  useNewUrlParser: true,
  reconnectTries: 60,
  reconnectInterval: 1000
}
const routes = require('./routes/routes.js')
const port = 80
const app = express()
const http = require('http').Server(app)

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use('/api', routes)
app.use((req, res) => {
  res.status(404)
})

MongoClient.connect(url, options, (err, database) => {
  if (err) {
    console.log(`FATAL MONGODB CONNECTION ERROR: ${err}:${err.stack}`)
    process.exit(1)
  }
  app.locals.db = database.db(databaseName)
  http.listen(port, () => {
    console.log("Listening on port " + port)
    app.emit('APP_STARTED')
  })
})

module.exports = app