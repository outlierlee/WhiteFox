
```cpp
#include <iostream>
#include <vector>
#include <array>
#include <string>
/*
// declare variables
*/
int x = 7; // declare x
unsigned y = 11; // declare y
float z = 1.5; // declare z

// define a function with non-local linkage (not static) that has unused parameters
int func_with_unused_params(int a, int b, int c) {
  int result = 0; // declare the result
  result += z + y; // Do something here, but don't use the parameters a, b, or c
  result += x; // result is related to x
  return result;
}

int main() { 
  std::cout << (x + y + z) << std::endl;
  int main_result = 0; // declare the result
  // invoke the func_with_unused_params
  // you can pass the arguments with any value, any type
  main_result = func_with_unused_params(x, y, z);
  return main_result; // return the result
}
``` 

