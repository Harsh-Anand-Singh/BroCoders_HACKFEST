const express = require('express');
const app2 = express();
app2.use(express.urlencoded({ extended: true }))
// Handle GET requests to the "/userdata" URL
app2.post('/userdata', (req, res) => {
    res.send(req.body);
});
app2.get('/', (req, res) => {
    res.send("Hello");
})

// Start the server
app2.listen(3000, () => {
    console.log('Server started on port 3000');
});