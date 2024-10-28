```c
#include <math.h>

// declare variables
int x = 20; // declare variable x, any value
char y = 'd'; // declare y, any value
float z = 10.456677; // declare z, any value

// define a function with non-local linkage (not static) that has unused parameters
int func_with_unused_params(int a, int b, int c) {
  int result = 0; // declare the result
  for(int i = 0; i < 1e20; i++) {
    result += rand() % 10;
  }
  result = pow(result, x);
  return result;
}

// main function which calls the func_with_unused_params function
int main() {
  int main_result = 0; // declare the result
  main_result = func_with_unused_params(x, y, z);
  return main_result; // return the result
}
``` 

