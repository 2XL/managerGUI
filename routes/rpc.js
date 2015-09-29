var express = require('express');
var router = express.Router();

var zerorpc = require('zerorpc');

var client = new zerorpc.Client();
client.connect('tcp://127.0.0.1:4242');

/* GET manager rpc page. */
router.get('/goodbye', function (req, res, next) {
    // el servidor rep una peticio get,
    client.invoke('goodbye', "Goodbye", function(error, resp, more) {
        if(error){
            console.log("Error:", error)
        }
        console.log(resp);
    });
    res.json({})

});





/* GET manager rpc page. */
router.get('/hello', function (req, res, next) {
    // el servidor rep una peticio get,

    client.invoke('hello', "Hello", function(error, resp, more) {
        if(error){
            console.log("Error:", error)
        }
        console.log(resp);
    });
    res.json({})

});



/* GET manager rpc page. */
router.get('/start', function (req, res, next) {
    // el servidor rep una peticio get,


    client.invoke('start', "Start", function(error, resp, more) {
        if(error){
            console.log("Error:", error)
        }
        console.log(resp);

    });
    res.json({})
});


/* GET manager rpc page. */
router.get('/cmd', function (req, res, next) {
    // el servidor rep una peticio get,


    client.invoke('cmd', "Cmd", function(error, resp, more) {
        if(error){
            console.log("Error:", error)
        }
        console.log(resp)
    });
    res.json({})
});


/* GET manager rpc page. */
router.get('/list', function (req, res, next) {
    // el servidor rep una peticio get,


    client.invoke('list', "~", function(error, resp, more) {
        if(error){
            console.log("Error:", error)
        }
        console.log(resp)

        res.json({result: JSON.stringify(resp)})
    });
});






module.exports = router;
