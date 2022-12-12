#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 100  // maximum length of the input sentence

int main() {
  char sentence[MAX_LENGTH];  // declare a char array to hold the sentence

  printf("Enter a sentence: ");  // prompt the user to enter a sentence
  fgets(sentence, MAX_LENGTH, stdin);  // read the sentence from standard input

  // remove the newline character at the end of the sentence
  sentence[strcspn(sentence, "\n")] = 0;

  printf("Your sentence is: %s\n", sentence);  // print out the sentence

  return 0;
}

// this is an example of clean code 
