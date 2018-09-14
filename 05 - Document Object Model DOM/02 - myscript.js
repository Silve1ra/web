var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

headOne.addEventListener('mouseover',function(){
    headOne.textContent = "Mouse currently over"
    headOne.style.color = 'red'
})

headOne.addEventListener('mouseout', function(){
    headOne.textContent = "Hover over me"
    headOne.style.color = 'black'
})

headTwo.addEventListener('click', function(){
    headTwo.textContent = 'Clicked on'
    headTwo.style.color = 'blue'
})

headTwo.addEventListener('dblclick', function(){
    headTwo.textContent = 'I was double clicked!'
    headTwo.style.color = 'red'
})

/*
headTwo.addEventListener('mouseout', function(){
    headTwo.textContent = 'Click me'
    headTwo.style.color = 'black'
})
*/