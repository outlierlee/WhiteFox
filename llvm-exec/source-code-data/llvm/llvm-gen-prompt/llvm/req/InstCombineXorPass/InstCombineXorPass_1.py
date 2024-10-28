#include <stdio.h>

// declare variables
ANY_TYPE a = ANY_VALUE; // declare a
ANY_TYPE b = ANY_VALUE; // declare b
ANY_TYPE c = ANY_VALUE; // declare c
ANY_TYPE d = ANY_VALUE; // declare d

int main() {
  // perform bitwise OR operations
  ANY_TYPE or1 = a | b;
  ANY_TYPE or2 = a | c;

  // perform XOR operation
  ANY_TYPE result = or1 ^ or2;

  // print the result
  printf("%d\n", result);

  return 0;
}
