
```c
#include <stdio.h>
#include <alloca.h>

void example_function() {
  int* a = alloca(sizeof(int));
  int* b = alloca(sizeof(int));

  *a = 100;
  *b = 200;

  *a = *a + *b;
  *b = *a * 2;

  printf("a: %d, b: %d\n", *a, *b);
}

int main() {
  example_function();
  return 0;
}
```
