/* Felipe Silveira */
/* Setembro de 2018 */
/* eng.fe.silveira@gmail.com*/

var firstName = prompt("First name please: ")
var lastName = prompt("Last name please: ")
var age = prompt("How old are you? ")
var height = prompt("What is your height? ")
var petName = prompt("What is your pet name? ")
alert("Thank you so much for the information!")

// logic

// four conditions
var nameCond = null;
var ageCond = null;
var heighCond = null;
var petCod = null;

// name condition
if(firstName[0] === lastName[0]){
    nameCond = true;
}else{
    nameCond = false;
}

// age condition
if(age > 20 && age < 30){
    ageCond = true;
}else{
    ageCond = false;
}

// height condition
if(height > 170){
    heighCond = true;
}else{
    heighCond = false;
}

// pet condition
if(petName[petName.length-1] === "y"){ //ultima letra do nome
    petCod = true;
}else{
    petCod = false;
}

// all conditions
if(nameCond && ageCond && heighCond && petCod){
    console.log("WELCOME SPY!")
}else{
    console.log("Nothing to see here")
}