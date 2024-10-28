
```c
#include <alloca.h>
#include <stdio.h>
#include <stdlib.h>

void example_function() {
  int *a = (int *) alloca(sizeof(int));
  int *b = (int *) alloca(sizeof(int));
  *a = 0; // Declare and initialize a variable
  *b = 1; // Declare and initialize another variable

  *a = *a + *b; // Simple arithmetic operation
  *b = *a * 2; // Another operation involving the variables

  printf("a: %d, b: %d\n", *a, *b);
}

int main() {
  example_function();
  return 0;
}
```
