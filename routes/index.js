var express = require('express');
var router = express.Router();


/* GET home page. */
router.get('/', function (req, res, next) {


    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    console.log('Client IP: ', ip);


    res.render('index', {title: 'Express'});
});

/* GET home page. */
router.get('/home', function (req, res, next) {
    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    console.log('Client IP: ', ip);


    res.render('home', {title: 'Home'});
});


module.exports = router;
