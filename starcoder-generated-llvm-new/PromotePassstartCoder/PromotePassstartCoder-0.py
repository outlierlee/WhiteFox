
```c
#include <stdio.h>
#include <alloca.h>

void example_function() {
  int a = (1 << 31); // Declare and initialize a variable
  int b = 1; // Declare and initialize another variable
  int c = 2; // Declare and initialize another variable

  // Use alloca
  int* d = (int*)alloca(5 * sizeof(int)); // Allocate memory on the stack

  // Use the allocated memory
  d[0] = a + b;
  d[1] = b + c;
  d[2] = a - c;

  // Use the variables
  a = d[0]; // Store the result back into a
  b = d[1]; // Store the result back into b
  c = d[2]; // Store the result back into c

  // Print the results to ensure the variables are used
  printf("a: %d, b: %d, c: %d\n", a, b, c);
}

int main() {
  example_function();
  return 0;
}
```

