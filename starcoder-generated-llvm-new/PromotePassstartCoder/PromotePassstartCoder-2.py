```
#include <stdio.h>
#include <alloca.h>

void example_function() {
  int* a = (int*)alloca(sizeof(int));
  int* b = (int*)alloca(sizeof(int));
  *a = 1000000000;
  *b = 4;
  *a = *a + *b;
  *b = *a * 2;
  printf("a: %d, b: %d\n", *a, *b);
}

int main() {
  example_function();
  return 0;
}
```
