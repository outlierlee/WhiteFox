
```cpp
#include <iostream>
#include <vector>
#include <string>

static void varargs_func(int x, ...) {
  for (int i = 0; i < x; ++i) {
    int flag = 0;
    if (i % 2) {
      flag = 1;
    }
    if (flag) {
      std::cout << "Flag is true, iteration " << i << "\n";
    } else {
      std::cout << "Flag is false, iteration " << i << "\n";
    }
  }
}

int main() {
  int x = 10;
  varargs_func(x, 1, 2, 3, 4, 5);
  return 0;
}
```

