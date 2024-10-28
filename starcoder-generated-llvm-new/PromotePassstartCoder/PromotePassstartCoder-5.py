
```c
#include <stdlib.h>
#include <stdio.h>

// Define a function that uses stack-allocated variables
void example_function() {
  int a;
  int b;

  // Align stack pointer
  register char *sp asm("sp");
  sp += (256 - ((long)sp & 255));

  // Allocate two variables on the stack with alloca
  a = *(int*)alloca(sizeof(int));
  b = *(int*)alloca(sizeof(int));

  // Initialize the variables
  a = 10;
  b = 20;

  // Perform operations on the variables
  a = a * b;
  b = a / 2;

  // Print the results
  printf("a: %d, b: %d\n", a, b);
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```
