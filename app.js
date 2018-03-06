


// const http = require('http')
// const port = 3000

// const requestHandler = (request, response) => {

//     console.log('Hello, node.js Server!')
// }

// const server = http.createServer(requestHandler) 

// server.listen(port, (err) => {

//     if (err) {

//         return console.log('Something bad happened', err)

//     }
//     console.log(`server is listering on ${port}`)
// })

var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello New York!!!!\n');
}).listen(3001);
console.log('Server running at http://localhost:3001/');