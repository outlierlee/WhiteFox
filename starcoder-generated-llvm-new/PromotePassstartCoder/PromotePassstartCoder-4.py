
```cpp
#include <stdio.h>
#include <alloca.h>

void example_function() {
  int* a = (int*)alloca(sizeof(int));
  int* b = (int*)alloca(sizeof(int));

  // Initialize variables
  *a = 0;
  *b = 1;

  // Use variables in a way that they can be promoted to registers
  *a = *a + *b;
  *b = *a * 2;

  printf("a: %d, b: %d\n", *a, *b);
}

int main() {
  example_function();
  return 0;
}
```

