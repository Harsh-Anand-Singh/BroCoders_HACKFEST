const express = require('express');
const app = express();

// Handle GET requests to the "/userdata" URL
app.get('/user', (req, res) => {
    res.send("this is it")
});
app.get('/', (req, res) => {
    res.send("Hello");
})

// Start the server
app.listen(3000, () => {
    console.log('Server started on port 3000');
});