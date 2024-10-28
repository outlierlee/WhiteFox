
```c
#include <alloca.h>
#include <stdio.h>

// Define a function that uses stack-allocated variables
void example_function() {
  // Declare variables using alloca
  int a; // Declare a variable with no initialization
  int b; // Declare another variable with no initialization
  a = 0; // Initialize a variable
  b = 1; // Initialize another variable

  // Use the variables in a way that they can be promoted to registers
  a = a + b; // Simple arithmetic operation

  // Print the results before promotion
  printf("a before promotion: %d\n", a);

  // Promote variables
  int* pa = (int*) alloca(sizeof(*pa)); // Allocate space in the stack
  int* pb = (int*) alloca(sizeof(*pb));
  *pa = a; *pb = b; // Write the variables to the stack

  // Print the results to ensure the variables are used
  printf("a after promotion but before free: %d, b: %d\n", *pa, *pb);

  // Free the space allocated on the stack
  // This is omitted for brevity, but it's generally a good idea
  // to free allocated memory to prevent memory leaks in production code.
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```

