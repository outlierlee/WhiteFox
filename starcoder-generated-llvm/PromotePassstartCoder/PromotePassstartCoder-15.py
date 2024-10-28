
```c
#include <stdio.h>
#include <alloca.h>

// Define a function that uses alloca-allocated variables
void example_function() {
  // Declare 2 variables using alloca
  int* a = (int*)alloca(sizeof(int)); // Declare and initialize a variable
  int* b = (int*)alloca(sizeof(int)); // Declare and initialize another variable

  // Allocate space for a bigger array
  int* big_array = (int*)alloca(1000 * sizeof(int));

  // Use the variables in a way that they can be promoted to registers
  *a = 10; // Simple arithmetic operation
  *b = 30; // Another operation involving the variables

  // Print the results to ensure the variables are used
  printf("a: %d, b: %d\n", *a, *b);
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```
