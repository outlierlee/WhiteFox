
```c
#include <stdio.h>

void example_func() {
  int n = 15;
  float pi = 3.14;
  char splChar = '@';
  char str[30] = "Hello, World!";
  n = n + 5;
  pi = pi * 2.0;
  splChar = '$';

  printf("Value of integer: %d\n", n);
  printf("Value of float: %f\n", pi);
  printf("Value of character: %c\n", splChar);
  printf("Value of string: %s\n", str);
}

int main() {
  example_func();
  return 0;// Return from main
}
```

