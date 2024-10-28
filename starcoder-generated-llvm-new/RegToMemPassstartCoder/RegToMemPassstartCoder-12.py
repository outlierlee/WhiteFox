```c
#include <stdio.h>

// Function declaration
int some_function(int x, char y, float z);

int main() {
  unsigned int a = 100;
  unsigned int b = 15;
  unsigned int c = 5;
  int d = some_function(a, 'A', 25.0);
  printf("%d\n", d);
  return d;
}

// Function definition
int some_function(int x, char y, float z) {
  int result = x + y;
  result -= z;
  return result;
}
```
