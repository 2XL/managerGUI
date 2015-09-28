var mongoose = require('mongoose');

var HostSchema = new mongoose.Schema({
    hostname: {type: String, default: 'toSet'},
    ip:  {type: String, default: 'localhost'},
    logging: {type: String, default: 'milax'},
    updated_at: { type: Date, default: Date.now }
});


module.exports = mongoose.model('Host', HostSchema);