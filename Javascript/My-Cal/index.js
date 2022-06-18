let num1El = parseInt(prompt("Enter the first number."))
let num2El = parseInt(prompt("Enter the second number."))
document.getElementById("num1-el").textContent = num1El
document.getElementById("num2-el").textContent = num2El

let sumEl = document.getElementById("sum-el")

function add() {
    let answer = num1El + num2El
    sumEl.textContent = answer
}

function subtract() {
    let answer = num1El - num2El
    sumEl.textContent = answer
}

function multiply() {
    let answer = num1El * num2El
    sumEl.textContent = answer
}

function divide() {
    let answer = num1El / num2El
    sumEl.textContent = answer
}
