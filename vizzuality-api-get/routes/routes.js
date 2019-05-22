const express = require('express')
const router = express.Router()

router.get('/emissions/all', (req, res, next) => {
    req.app.locals.db.collection('emissions').find({}).toArray((err, result) => {
        if (err) {
            res.status(400).send({'error': err})
        }
        if (result === undefined || result.length === 0) {
            res.status(400).send({'error':'No documents in database'})
        } else {
            res.status(200).send(result)
        }
    })
})

router.get('/emissions/country/:country', (req, res, next) => {
    req.app.locals.db.collection('emissions').find(
        {'Country': req.params.country}).toArray((err, result) => {
        if (err) {
          res.status(400).send({'error': err})
        }
        if (result === undefined || result.length === 0) {
          res.status(400).send({'error':'No documents in database'})
        } else {
          res.status(200).send(result)
        }
      })
})

router.get('/emissions/sector/:sector', (req, res, next) => {
    req.app.locals.db.collection('emissions').find(
        {'Sector': req.params.sector}).toArray((err, result) => {
        if (err) {
          res.status(400).send({'error': err})
        }
        if (result === undefined || result.length === 0) {
          res.status(400).send({'error':'No documents in database'})
        } else {
          res.status(200).send(result)
        }
      })
})

router.get('/emissions/parentsector/:parentsector', (req, res, next) => {
    req.app.locals.db.collection('emissions').find(
        {'Parent sector': req.params.parentsector}).toArray((err, result) => {
        if (err) {
          res.status(400).send({'error': err})
        }
        if (result === undefined || result.length === 0) {
          res.status(400).send({'error':'No documents in database'})
        } else {
          res.status(200).send(result)
        }
      })
})

module.exports = router