var zerorpc = require("zerorpc");

var client = new zerorpc.Client();
client.connect("tcp://127.0.0.1:4242");



client.invoke("hello", "Chenglong", function(error, res, more) {
    console.log(res);
});



client.invoke("goodbye", "Chenglong", function(error, res, more) {
    console.log(res);
});


client.invoke("bad", function(error, res, more){
    console.error("An error occurred: ", error)
})