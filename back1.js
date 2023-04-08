const express = require('express');
const spawn = require('child_process').spawn;

const app2 = express();
app2.set('view engine','ejs');
app2.use(express.urlencoded({
    extended: true
}));
app2.post('/ala', (req, res) => {
    const pyone = spawn("C:/Users/dasar/AppData/Local/Programs/Python/Python310/python.exe", ['ala.py', parseInt(req.body.department), parseInt(req.body.semester), parseInt(req.body.pf1), parseInt(req.body.pf2), parseInt(req.body.pf3), parseInt(req.body.pf4), parseInt(req.body.pf5)]);
    let stdoutBuffer = '';
    let stderrBuffer = '';
    pyone.stdout.on('data', function (data) {
        stdoutBuffer += data.toString();
    });
    pyone.stderr.on('data', function (data) {
        stderrBuffer += data.toString();
    });
    pyone.on('close', (code) => {
        console.log("code", code);
        if (stdoutBuffer.length === 0 && stderrBuffer.length === 0) {
            res.send("No data received from child process");
        } else {
            res.send(stdoutBuffer + stderrBuffer);
        }
    });
})
// Handle POST requests to the "/user" route
app2.post('/user', (req, res) => {
    console.log(req.body);
    res.send(req.body.department);
});

// Start the server
app2.listen(3000, () => {
    console.log('Server started on port 3000');
});
