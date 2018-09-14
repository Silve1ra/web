/* Felipe Silveira */
/* Setembro de 2018 */
/* eng.fe.silveira@gmail.com*/

function hello (){
    console.log("Hello world!");
    
}

function helloYou(name){
    console.log("Hello "+name);
    
}

function addNum(num1, num2){
    console.log(num1+num2);
    
}

function helloSomeone(name="Juliana"){ //fica default
    console.log("Hello "+name);
    
}

function formal(name="Felipe", title="Sir"){
    return title+ " "+name
}

function timesFive(numInput){
    var result = numInput*5
    return result
}

var v = "GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff){
    console.log(v);
    stuff = "lalalala"
    console.log(stuff);
    
    
}