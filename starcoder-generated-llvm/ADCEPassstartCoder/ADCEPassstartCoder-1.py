
```cpp
#include <iostream>

// declare variables
float a = 1.1; // declare and initialize a
float b = 2.2; // declare and initialize b
float d = 0;   // declare and initialize d which would not cause a warning by compiling

// define a function that performs some operations
float compute(float x, float y) {
  float result = x + y; // perform an operation
  return result; // return the result
}

int main() {
  float main_result = 0; // declare the result

  // perform some operations
  float c = compute(a, b); // perform an operation using the function compute and store the result in variable 'c'

  // invoke the compute function and then perform some operations, none of which are connected to the result
  // pitfall example: d = a + b; which could be removed by any optimizing tool

  // print the result
  // here d is not used or directly connected with the result. 
  // The following statement is a direct typecast. It will not cause any output to the console and is thus not in the scope of the optimization
  std::cout << d * a; 

  return 0; // return the result
}
```
