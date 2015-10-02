var express = require('express');
var router = express.Router();
var queryString = require('query-string');
var zerorpc = require('zerorpc');



/* GET manager rpc page. */
router.get('/goodbye', function (req, res, next) {

    var client = new zerorpc.Client({
        timeout: 3000,  // Sets the number of seconds to wait for a response before considering the call timed out. Defaults to 30.
        heartbeatInterval: 100000 // Sets the number of miliseconds to send send heartbeats to connected servers. Defaults to 5000ms.
    });
    client.connect('tcp://127.0.0.1:4242');

    // el servidor rep una peticio get,
    client.invoke('goodbye', "Goodbye", function (error, resp, more) {
        if (error) {
            console.log("Error:", error)
        }
        console.log(resp);

        res.json(resp)
    });

});


/* GET manager rpc page. */
router.get('/hello', function (req, res, next) {

    var client = new zerorpc.Client({
        timeout: 3000,  // Sets the number of seconds to wait for a response before considering the call timed out. Defaults to 30.
        heartbeatInterval: 100000 // Sets the number of miliseconds to send send heartbeats to connected servers. Defaults to 5000ms.
    });
    client.connect('tcp://127.0.0.1:4242');

    // el servidor rep una peticio get,

    client.invoke('hello', "Hello", function (error, resp, more) {
        if (error) {
            console.log("Error:", error)
        }
        console.log(resp);

        res.json(resp)
    });

});


/* GET manager rpc/rpc page. */
router.get('/rpc', function (req, res, next) {

    var client = new zerorpc.Client({
        timeout: 3000,  // Sets the number of seconds to wait for a response before considering the call timed out. Defaults to 30.
        heartbeatInterval: 100000 // Sets the number of miliseconds to send send heartbeats to connected servers. Defaults to 5000ms.
    });
    client.connect('tcp://127.0.0.1:4242');

    // el servidor rep una peticio get,
    console.log('RPC/RPC');
    console.log(req.url);
    var fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;

    // this is  blocking the code...
    client.invoke('rpc', fullUrl, function (error, resp, more) {
        if (error) {
            console.log("Error:", error)
        }
        console.log(resp);
        res.json(resp)
    });

});



/* GET manager rpc page. */
router.get('/start', function (req, res, next) {

    var client = new zerorpc.Client({
        timeout: 3000,  // Sets the number of seconds to wait for a response before considering the call timed out. Defaults to 30.
        heartbeatInterval: 100000 // Sets the number of miliseconds to send send heartbeats to connected servers. Defaults to 5000ms.
    });
    client.connect('tcp://127.0.0.1:4242');

    // el servidor rep una peticio get,


    client.invoke('start', "Start", function (error, resp, more) {
        if (error) {
            console.log("Error:", error)
        }
        console.log(resp);

        res.json(resp)
    });
});


/* GET manager rpc page. */
router.get('/nmap', function (req, res, next) {

    var client = new zerorpc.Client({
        timeout: 3000,  // Sets the number of seconds to wait for a response before considering the call timed out. Defaults to 30.
        heartbeatInterval: 100000 // Sets the number of miliseconds to send send heartbeats to connected servers. Defaults to 5000ms.
    });
    client.connect('tcp://127.0.0.1:4242');

    // el servidor rep una peticio get,
    //console.log(req.params)
    console.log("COMMAND: ");
    console.log(req.url)
    var cmd = req.url.split('=')[1].replace(/\+/g, ' ');
    console.log(cmd);
    //console.log(" ex: ------------->", queryString.extract(req.params));
    //console.log(" ex: ------------->", queryString.parse(req.params));
    // console.log(" parse: --> Query String", queryString.parse(location.search))

    client.invoke('nmap', cmd.split(' ')[1], cmd.split(' ')[0], function (error, resp, more) {
        if (error) {
            console.log("Error:", error)
        }
        console.log(resp);



        res.json({result: JSON.stringify(resp)})
    });
});


/* GET manager rpc page. */
router.get('/list', function (req, res, next) {

    var client = new zerorpc.Client({
        timeout: 3000,  // Sets the number of seconds to wait for a response before considering the call timed out. Defaults to 30.
        heartbeatInterval: 100000 // Sets the number of miliseconds to send send heartbeats to connected servers. Defaults to 5000ms.
    });
    client.connect('tcp://127.0.0.1:4242');

    // el servidor rep una peticio get,


    client.invoke('list', "~", function (error, resp, more) {
        if (error) {
            console.log("Error:", error)
        }
        console.log(resp);

        res.json({result: JSON.stringify(resp)})
    });
});

/* GET manager rpc page. */
router.get('/cmd', function (req, res, next) {

    var client = new zerorpc.Client({
        timeout: 3000,  // Sets the number of seconds to wait for a response before considering the call timed out. Defaults to 30.
        heartbeatInterval: 100000 // Sets the number of miliseconds to send send heartbeats to connected servers. Defaults to 5000ms.
    });
    client.connect('tcp://127.0.0.1:4242');

    // el servidor rep una peticio get,
    //console.log(req.params)
    console.log("COMMAND: ");
    console.log(req.url);
    var cmd = req.url.split('=')[1].replace(/\+/g, ' ');
    // cmd = JSON.stringify(cmd);
    console.log(cmd);
    //console.log(" ex: ------------->", queryString.extract(req.params));
    //console.log(" ex: ------------->", queryString.parse(req.params));

    // console.log(" parse: --> Query String", queryString.parse(location.search))


    (client.invoke('cmd', cmd, function (error, resp, more) {
        if (error) {
            console.log("Error:", error)
        }
        // console.log(JSON.stringify(resp))

        res.json({result: JSON.stringify(resp)})
    }));
});


module.exports = router;
