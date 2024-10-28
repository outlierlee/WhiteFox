
```c
#include <stdio.h>

int a = 92384; // declare a
int b = 38400; // declare b
int c = 19038; // declare c

int main() {
  int result = 0; // declare the result

  result = (a + b) + c; // associative operation
  result = (result * a) * b; // another associative operation
  result = (result - c) - a; // yet another associative operation

  printf("%d\n", result);

  return 0;
}
```

