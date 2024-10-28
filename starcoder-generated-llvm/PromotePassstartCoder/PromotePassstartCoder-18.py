
```cpp
#include <alloca.h>
#include <stdio.h>

// Define a function that uses stack-allocated variables
void example_function() {
  // Declare and initialize variables using alloca
  auto a = static_cast<int*>(alloca(sizeof(int)));
  auto b = static_cast<int*>(alloca(sizeof(int)));
  *a = 0; // Declare and initialize a variable
  *b = 1; // Declare and initialize another variable

  // Use the variables in a way that they can be promoted to registers
  *a = *a + *b; // Simple arithmetic operation
  *b = *a * 2; // Another operation involving the variables

  // Print the results to ensure the variables are used
  printf("a: %d, b: %d\n", *a, *b);
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```

