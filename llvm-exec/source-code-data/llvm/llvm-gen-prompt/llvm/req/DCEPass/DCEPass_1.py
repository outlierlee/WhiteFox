#include <stdio.h>

// declare variables
int x = ANY_VALUE; // declare x
ANY_TYPE y = ANY_VALUE; // declare y
ANY_TYPE z = ANY_VALUE; // declare z

int main() {
  int main_result = 0; // declare the result

  // perform some operations that result in dead code
  int unused_var = x OPERATOR ANY_VALUE; // this operation is not used anywhere

  // use some variables in a way that does not affect the unused_var
  main_result = y OPERATOR z; // perform some operation with y and z

  printf("%d\n", main_result); // print the result to ensure side effects

  return main_result; // return the result
}
