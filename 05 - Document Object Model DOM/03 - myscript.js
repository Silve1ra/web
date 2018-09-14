//console.log("connected")

//restart game button
var restart = document.querySelector('#b')

//grabs all the squares
var squares = document.querySelectorAll('td')

//clear all the squares
function clearBoard(){
    for(var i=0; i<squares.length; i++){
        squares[i].textContent = ''
    }
}

restart.addEventListener('click', clearBoard)

//check the square marker

/*
jeito easy
var cellOne = document.querySelector('#one')

cellOne.addEventListener('click', function(){
    if (cellOne.textContent ===''){
        cellOne.textContent = 'X'
    }else if(cellOne.textContent === 'X'){
        cellOne.textContent='O'
    }else{
        cellOne.textContent=''
    }
})
*/

/* jeito hard */
function changeMarker(){
    if(this.textContent === ''){
        this.textContent = 'X'
    }else if (this.textContent === 'X'){
        this.textContent = 'O'
    }else{
        this.textContent = ''
    }
}

for (var i=0; i<squares.length; i++){
    squares[i].addEventListener('click', changeMarker)
}

//for loop to add event listeners to all the squares