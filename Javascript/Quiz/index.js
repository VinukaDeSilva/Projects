// Question 1
let questionEl = "Who is Harry Potter's godfather?"
document.getElementById("question-el").textContent = questionEl

let answerEl = document.getElementById("answer-el")

function a() {
    let ANSWER = "Woohooo! Correct answer!!"
    answerEl.textContent = ANSWER
    score += 1
}

function b() {
    let ANSWER = "Sorry, wrong answer...."
    answerEl.textContent = ANSWER
}

function c() {
    let ANSWER = "Sorry, wrong answer...."
    answerEl.textContent = ANSWER
}
