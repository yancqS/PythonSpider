"use strict";
var page = require('webpage').create();
var system = require('system');
var t, address;

if(system.args.length === 1){
    console.log('Usage: loadspeed.js <some URL>');
    phantom.exit();
}
t = Date.now();
address = system.args[1];
page.open(address, function(status){
    if(status !== 'success'){
        console.log("Unload the address");
    }else{
        t = Date.now() - t;
        console.log("load address:",address);
        console.log("load time:",t,"mesc");
    }
    phantom.exit();
});
