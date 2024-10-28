
```c
#include <stdio.h>

int global_var1 = 42;
float global_var2 = 3.14;

void external_func1() {
  printf("Hello from external_func1\n");
}

void external_func2() {
  printf("Hello from external_func2\n");
}

int main() {
  global_var1 += 10;
  external_func1();
  external_func2();

  return 0;
}
```
