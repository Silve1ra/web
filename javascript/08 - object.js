var employee = {
    name: "Miau shh",
    job: "Pet",
    age: 12,

    nameLength: function(){
        console.log(this.name.length)
    }
}

var employeev2 = {
    name: "Miau shh",
    job: "Pet",
    age: 12,

    report: function(){
        alert("Name is "+this.name+", Job is: "+this.job+", Age is: "+this.age)
    }
}

var employeev3 = {
    name: "Miau shh",
    job: "Pet",
    age: 12,

    lastName: function(){
        console.log(this.name.split(" ")[1])
    }
}