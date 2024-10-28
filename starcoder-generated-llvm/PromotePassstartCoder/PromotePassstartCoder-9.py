
```c
#include <alloca.h>
#include <stdio.h>

// Define a function that uses stack-allocated variables
void example_function() {
  // Declare variables using alloca
  int a = alloca (sizeof (int)); // Declare and initialize a variable
  int b = alloca (sizeof (int)); // Declare and initialize another variable

  // Use the variables in a way that they can be promoted to registers
  *(int*)a += 1; 
  *(int*)b *= 2; 

  // Print the results to ensure the variables are used
  printf("a: %d, b: %d\n", *(int*)a, *(int*)b);
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```
