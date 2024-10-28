
```c
#include <stdio.h>

int global_var1;
int global_var2 = 42;
float global_var3 = 3.14f;

static void external_func1() {}

void external_func2() {}

int main() {
  int c = 100;
  float b = 8.2f;
  extern int e;
  global_var1 += 1;  
  global_var2 -= 1;  
  global_var3 += 1;
  external_func1();  
  external_func2();
  printf("global: %d, %.2f\n", global_var2, global_var3);
  return 0;
}
```
