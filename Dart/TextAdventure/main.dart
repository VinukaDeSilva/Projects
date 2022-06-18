// importing the module
import 'dart:io';

void main() {
  // Creating the character
  stdout.writeln("Enter your name:");
  var name = stdin.readLineSync();
  print("Hello $name.");

  stdout.writeln("Are you a male or a female?");
  var Gender = stdin.readLineSync();
  if (Gender == 'male') {
    print("So, you are a male by the name of $name? (y/n)");

    var confirmation = stdin.readLineSync();
    if (confirmation == 'y') {
      print("Okay then, let's get started...");
    } else {
      print(
          "Sorry, but you cannot change your character name and gender once chosen.");
    }
  } else if (Gender == 'female') {
    print("So, you are a female by the name of $name? (y/n)");

    var confirmation = stdin.readLineSync();
    if (confirmation == 'y') {
      print("Okay then, let's get started...");
    } else {
      print(
          "Sorry, but you cannot change your character name and gender once chosen.");
    }
  } else {
    print("Error!!! Please restart the programme and try again.");
  }

  // beginning
  print(
      "Welcome to the world of pokemon. You are a 10 year old with a great desire to be the best and to catch them all. You start your journey in your room and from here, you will go to get your first pokemon and then your adventure begins.");
  // A welcome to the world.
  print("Hello, its time to get ready to start your journey now....");
  // A bit of information about the controls
  print(
      "Oh, I almost forgot to tell you. You will be given options and based on those you muct press the corresponding button to interact with the world around you");
  // You get to move around the house a bit
  print("Let's start....");

  stdout.writeln("""
1. Get dressed
2. Go downstairs
3. Go back to sleep😴
""");
  var O1 = stdin.readLineSync();
  if (O1 == "1") {
    print("You got dressed.");
  } else if (O1 == "2") {
    print("You go downstairs and your mother is there. She says 'Oh, good morning. Professor Gizmo was he earlier looking for you. He sould be in his lab now.'");
  } else if (O1 == "3") {
    print("You went to bed and woke up. It looks like you left your adventure too early and woke up to a dream. Better luck next time.");
  } else {
    print("Error!!!");
  }

  // Find professor Gizmo to get your first pokemon.

  // level 1 cave
}
