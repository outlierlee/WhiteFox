
```c++
#include <alloca.h>
#include <stdio.h>

// Define a function that uses stack-allocated variables
void example_function() {
  // Declare variables using alloca
  int a = (1 << 31); // Declare and initialize a variable
  void* v = alloca(sizeof(int)); // Allocate space for a variable

  // Use the variables in a way that allows them to be promoted to registers
  *((int*)v) = a + 3; // Simple arithmetic operation
  a = *((int*)v) * 2; // Another operation involving the variables

  // Print the results to ensure the variables are used
  printf("a: %d\n", a);
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```
