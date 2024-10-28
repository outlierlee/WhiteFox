
```c
#include <iostream>
#include <vector>

int global_var1;
float global_var2;

static void external_func1() {
  global_var1 += 100;
}

static void external_func2() {
  global_var2 += 2.5;
}

int main() {
  global_var1 = 10;
  global_var2 = 3.14;
  external_func1();
  external_func2();
  global_var1 -= 5;
  return global_var1;
}
```

