let num1 = 0
let sumEl = document.getElementById('sum-el')
sumEl.textContent = num1

function add() {
    // adding function
    num1 += 1
    sumEl.textContent = num1
}

function sub() {
    // subtracting function
    num1 -= 1
    sumEl.textContent = num1
}