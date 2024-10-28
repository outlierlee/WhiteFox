
```c
#include <alloca.h>
#include <stdio.h>

void example_function() {
  int *a =(int *)alloca(sizeof(int));
  int *b =(int *)alloca(sizeof(int));
  *a = 0;
  *b = 1;

  // Use the variables in a way that slows down the function so it can be optimized
  for (int i = 0; i < 1000000000; i++) {
    *a = *a + *b;
    *b = *a * 2;
  }

  // Print the results to ensure the variables are used
  printf("a: %d, b: %d\n", *a, *b);
}

int main() {
  // Call the function
  example_function();
  return 0;
}
```
