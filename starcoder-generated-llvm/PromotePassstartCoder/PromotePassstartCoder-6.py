
```c
#include <alloca.h>
#include <stdio.h>

void varargs_func() {
  // Declare variables using alloca
  int a = 0; // Declare and initialize a variable
  int b = 1; // Declare and initialize another variable

  // Use the variables in a way that they can be promoted to registers
  a = a + b; // Simple arithmetic operation
  b = a * 2; // Another operation involving the variables

  // Print the results to ensure the variables are used
  printf("a: %d, b: %d\n", a, b);
}

int main() {
  // Call the function
  varargs_func();
  return 0;
}
```

