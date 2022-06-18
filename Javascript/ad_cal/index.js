// let num1 = parseInt(prompt("Enter the first number: "))
// let num2 = parseInt(prompt("Enter the second number: "))
document.getElementById("num1-el").textContent = num1
document.getElementById("num2-el").textContent = num2

let sumEl = document.getElementById("sum-el")

function add() {
    let SUM = num1 + num2
    sumEl.textContent = SUM
}

function sub() {
    sumEl.textContent = num1 - num2
}

function multiply() {
    sumEl.textContent = num1 * num2
}

function divide() {
    sumEl.textContent = num1 / num2
}
