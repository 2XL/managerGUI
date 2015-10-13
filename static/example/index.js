(function () {
    var jsonDesc;
    // var demoURL = 'https://ast03:8443/render?target=benchbox.ast04.StackSync.cpu_usage&format=json'
    var demoURL1 = 'https://ast03:8443/render?target=collectd.graphite.entropy.entropy&format=json'
    var demoURL2 = 'https://ast03:8443/render?target=collectd.graphite.entropy.entropy&format=json'
    var demoURL = 'https://ast03:8443/render?target=collectd.graphite.processes.fork_rate&format=json'
    jsonDesc = {
        "Total Notifications": {
            source: demoURL,
            GaugeLabel: {
                parent: "#hero-one",
                observer: function (data) {
                    console.log("Label observing " + data);
                },
                title: "Notifications Served",
                type: "max"
            }
        },
        "Poll Time": {
            source: demoURL1,
            GaugeGadget: {
                parent: "#hero-two",
                title: "P1",
                observer: function (data) {
                    console.log("Gadget observing " + data);
                }
            }
        },

        /*

        "Total Installs": {
            source: demoURL,
            GaugeLabel: {
                parent: "#hero-three",
                title: "Clients Installed"
            }
        },
        "Clients 1": {
            source: demoURL,
            GaugeGadget: {
                parent: "#hero-three",
                title: "Cl1"
            }
        },
        */
        /*
        "New Message": {
            source: demoURL,
            TimeSeries: {
                parent: '#g1-1',
                title: 'New Message',
                label_offset: 200,
                label_columns: 2,
                time_span_mins: 12,
                observer: function (data) {
                    console.log("Time series observing ", data);
                }
            }
        },
        */
        "Fork Rate": {
            source: demoURL,
            TimeSeries: {
                title: 'Fork Rate',
                warn: 600,
                error: 800,
                parent: '#g2-1'
            }
        }
        /*
        "Foo Work": {
            source: demoURL,
            BarChart: {
                parent: '#g2-3'
            }
        }
        */
    };


     var g = new Graphene;
     // g.demo();
     g.build(jsonDesc);



    /*
    var g = new Graphene;
    g.discover('https://10.30.103.95:8443', 'benchbox',
        function (i, url) {
            return  '#g2-3'
        },
        function (description) {
            g.build(description);
            console.log(description)

        })
    */

}).call(this);