
```c
#include <alloca.h>
#include <stdio.h>

void example_function() {
  int* a = (int*)alloca(sizeof(int)); // Use alloca for stack allocation and cast to int*
  int* b = (int*)alloca(sizeof(int));
  *a = 0; // Dereference and assign to allocate a value
  *b = 1;
  *a = *a + *b; // Add the values
  *b = *a * 2; // Multiply the added values
  printf("a: %d, b: %d\n", *a, *b); // print values
}

int main() {
  example_function();
  return 0;
}
```

