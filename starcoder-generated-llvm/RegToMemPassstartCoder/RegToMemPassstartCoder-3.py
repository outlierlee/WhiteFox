
```c
#include <stdio.h>

void example_function() {
  int a = 1 << 31;
  float b = 1.000000;
  char c = 'A';
  
  a += 5;
  b = b * 30;
  c = 'B';
  
  printf("a: %d, b: %f, c: %c\n", a, b, c);
}

int main() {
  example_function();
  return 0;
}
```
