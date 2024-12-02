// Steps to run
// npm install express request
// node ip-ap.js
// Visit http://localhost:3000/{ip}

const express = require('express')
const request = require('request')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.set('json spaces', 4)

app.get('/:id', (req, res) => { 
  const ip = req.params.id;
  request(`http://ip-api.com/json/${ip}`, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    const json = JSON.parse(body);
  	res.send(json)
  }
})

}); 

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})