// importing the module
import 'dart:io';

// Creating the lists
var Questions = ["How old was Harry Potter when he 'died'?", "When was the first Harry Potter movie released?", "Who was the ruler of Germany during WW2?"];
var Answers = ['17', '2001', 'Adolf Hitler'];

var ListLength = Questions.length; // A function that returns the length of the list

// The scoring system
int score = 0;

// Defining the function
void quiz(int QuestionNumber, int QuestionAnswer) {
  var Question = Questions[QuestionNumber];
  var Answer = Answers[QuestionAnswer];

  // Getting user input
  stdout.writeln(Question);
  var UserInput = stdin.readLineSync();

  // Checking if the input matches with the expected answer
  if (UserInput?.toLowerCase() == Answer.toLowerCase()) {
    print("That is correct!");

    // Using the scoring system
    score += 1;

  } else {
    print("That is incorrect. The correct answer is $Answer");
  }
}

void main() {
  quiz(0, 0);
  quiz(1, 1);
  quiz(2, 2);

  print("The score is $score out of $ListLength.");
}