const express = require('express');
const spawn = require('child_process').spawn;

const app2 = express();
app2.use(express.static(__dirname + '/public'));
app2.set('view engine', 'ejs');
app2.use(express.urlencoded({
    extended: true
}));
const re = require("./convert.json");
app2.post('/ala', (req, res) => {
    const pyone = spawn("C:/Users/dasar/AppData/Local/Programs/Python/Python310/python.exe", ['ala.py', parseInt(re["RTC"][req.body.department]), parseInt(req.body.semester), parseInt(re["RTC"][req.body.pf1]), parseInt(re["RTC"][req.body.pf2]), parseInt(re["RTC"][req.body.pf3]), parseInt(re["RTC"][req.body.pf4]), parseInt(re["RTC"][req.body.pf5])]);
    let stdoutBuffer = "";
    let stderrBuffer = "";
    console.log(parseInt(re["RTC"][req.body.department]), parseInt(req.body.semester), parseInt(re["RTC"][req.body.pf1]), parseInt(re["RTC"][req.body.pf2]), parseInt(re["RTC"][req.body.pf3]), parseInt(re["RTC"][req.body.pf4]), parseInt(re["RTC"][req.body.pf5]));
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
            const t = parseInt(stdoutBuffer);
            console.log(t);
            res.render('home.ejs', { result: re["CTR"][t] });
            
            console.log(re["CTR"][t]);
        }
    });
})

app2.post('/user', (req, res) => {
    console.log(req.body);
    res.send(req.body.department);
});

app2.post('/comment', (req, res) => {
    const fs = require('fs');


    fs.readFile('usercomment.json', 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            return;
        }
        const jsonData = JSON.parse(data);
        jsonData[req.body.course].push({
            "comment": req.body.comment,
            "author": req.body.name
        });
        fs.writeFile('usercomment.json', JSON.stringify(jsonData), (err) => {
            if (err) {
                console.error(err);
                return;
            }
            console.log('Data added successfully');
        });
    })
});
app2.listen(3000, () => {
    console.log('Server started on port 3000');
});
