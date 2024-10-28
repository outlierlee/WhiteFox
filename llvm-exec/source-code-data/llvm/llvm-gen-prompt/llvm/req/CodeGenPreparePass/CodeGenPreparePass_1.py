#include <stdio.h>

// Define a function with a switch statement
int switch_func(int x) {
  int result = 0; // declare the result
  switch (x) {
    case 1:
      result = x + 1;
      break;
    case 2:
      result = x + 2;
      break;
    default:
      result = x + 3;
      break;
  }
  return result;
}

int main() {
  int main_result = 0; // declare the result
  int x = 1; // initialize x with a constant value
  main_result = switch_func(x); // call the function with a constant argument
  printf("%d\n", main_result); // print the result
  return main_result; // return the result
}
