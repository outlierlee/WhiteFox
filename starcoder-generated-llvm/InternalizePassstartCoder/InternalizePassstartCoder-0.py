
```cpp
#include <iostream>

static int static_global_var = 44;

void func1();
void func2();

void func1() {
  static_global_var += 10;
}

void func2() {
  static_global_var *= 2;
}

int main() {
  func1();
  func2();
  return static_global_var;
}
```

