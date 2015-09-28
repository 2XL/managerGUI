var express = require('express');
var router = express.Router();

var zerorpc = require('zerorpc');


/* GET manager rpc page. */
router.get('/goodbye', function (req, res, next) {
    // el servidor rep una peticio get,

    var client = new zerorpc.Client();
    client.connect('tcp://127.0.0.1:4242');

    client.invoke('hello', "Goodbye", function(error, res, more) {
        console.log(res);
    });


});





/* GET manager rpc page. */
router.get('/hello', function (req, res, next) {
    // el servidor rep una peticio get,

    var client = new zerorpc.Client();
    client.connect('tcp://127.0.0.1:4242');

    client.invoke('hello', "Hello", function(error, res, more) {
        console.log(res);
    });


});



/* GET manager rpc page. */
router.get('/start', function (req, res, next) {
    // el servidor rep una peticio get,

    var client = new zerorpc.Client();
    client.connect('tcp://127.0.0.1:4242');

    client.invoke('start', "Start", function(error, res, more) {
        console.log(res);
    });
});


/* GET manager rpc page. */
router.get('/cmd', function (req, res, next) {
    // el servidor rep una peticio get,

    var client = new zerorpc.Client();
    client.connect('tcp://127.0.0.1:4242');

    client.invoke('cmd', "cmd", function(error, res, more) {
        console.log(res);
    });
});






module.exports = router;
