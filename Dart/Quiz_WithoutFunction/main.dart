// Importing the dart:io module that provides the functions to make this possible.
import 'dart:io';

// The main function
void main() {
  // Asking for player name
  stdout.writeln("Enter your name: ");
  var Name = stdin.readLineSync();
  print("Hello $Name.");

  // The scoring system
  int score = 0;
  int totalScore = 2;

  // Asking if the player wants to play this game
  stdout.writeln("Would you like to play this game $Name?");
  var wouldYouLikeToPlay = stdin.readLineSync();
  // An if conditional to see if yes or no
  if (wouldYouLikeToPlay?.toLowerCase() == "yes") {
    print("Let's get started....");

    // The first question
    stdout.writeln(
        "Question 1: What is the full name of the main protagonist of the Harry Potter series?");
    var Q1 = stdin.readLineSync();
    if (Q1?.toLowerCase() == "harry james potter") {
      print("That is correct!");
      score += 1;
    } else {
      print("That is wrong!");
    }

    // The second question
    stdout.writeln("Question 2: What is the total of 21 and 34?");
    var Q2 = stdin
        .readLineSync(); // var changed this to a string for some reason. Find out why...
    Q2 == double.parse(Q2!);  // Changed the value to a real number using the parse method
    if (Q2 == '55') {
      print("That is correct!");
      score += 1;
    } else {
      print("That is wrong!");
    }

    print(
        "The total score that you have accumulated is $score out of $totalScore, $Name. Hope you enjoyed this game. Goodbye....");
  } else {
    print("Let's play later then....");
  }
}
