var express = require('express');
var router = express.Router();
var fs = require('fs');

var sess;
/* GET init page. */
router.get('/', function (req, res, next) {
    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    console.log('Client IP: ', ip);
    var sess = req.session;

    var obj;

    fs.read('/js/config.js', function(err, data){
        if(err) throw err;
        obj = JSON.parse(data);
    });


    console.log("Session", sess);

    res.render('init', {title: 'Init'});
});



module.exports = router;
