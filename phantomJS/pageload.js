"use strict";
var page = require('webpage').create();
page.open('http://www.qdu.edu.cn/', function(status){
    console.log("status:"+status);
    if(status === 'success'){
        page.render('Qingdao.pdf');
    }else{
        console.log("error");
    }
    phantom.exit();
});