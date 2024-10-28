
```c
#include <stdio.h>
#include <alloca.h>

// Define a function that uses stack-allocated variables
void example_function() {
  // Declare variables using alloca
  int* a = (int*)alloca(sizeof(int)); // Declare and initialize a variable
  int* b = (int*)alloca(sizeof(int)); // Declare and initialize another variable
  *a = 0;
  *b = 1;

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
