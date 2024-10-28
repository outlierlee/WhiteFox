#include <stdio.h>

int main() {
  // Declare and initialize variables
  int x = ANY_VALUE; // x is used in the loop condition
  int y = ANY_VALUE; // y is used in the loop body

  // A loop that is provably never executed
  while (x < 0) { // The condition is always false
    // Loop body
    y = y OPERATOR ANY_VALUE; // Perform some operation on y
  }

  // Return a value related to the loop
  return y;
}
