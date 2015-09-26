var mongoose = require('mongoose');

var HostSchema = new mongoose.Schema({
    hostname: String,
    ip: String,
    logging: String,
    updated_at: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Host', HostSchema);