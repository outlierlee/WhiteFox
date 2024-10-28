
```cpp
#include <cstddef>
#include <iostream>

// Define a function that uses stack-allocated variables
void example_function() {
  // Declare variables using alloca
  int* a = (int*)alloca(sizeof(int)); // Declare and initialize a variable
  int* b = (int*)alloca(sizeof(int)); // Declare and initialize another variable

  // Use the variables in a way that they can be promoted to registers
  *a = 0; // Set the value of a
  *b = 4; // Set the value of b
  *a = *a + *b; // Simple arithmetic operation
  *b = *a * 2; // Another operation involving the variables

  // Print the results to ensure the variables are used
  std::cout << "a: " << *a << ", b: " << *b << std::endl;
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```
