
```c
#include<stdio.h>

static int my_function(int a, int b) {
  int result = 0;
  result = a + b;
  return result;
}

int main() {
  int a = 5;
  int b = 10;
  int main_result = 0;

  main_result = my_function(a, b);

  return main_result;
}
```
