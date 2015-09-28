var express = require('express');
var router = express.Router();

var sess;
/* GET init page. */
router.get('/', function (req, res, next) {
    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    console.log('Client IP: ', ip);
    var sess = req.session;

    console.log("Session", sess);

   res.render('init', {title: 'Init'});
});



module.exports = router;
