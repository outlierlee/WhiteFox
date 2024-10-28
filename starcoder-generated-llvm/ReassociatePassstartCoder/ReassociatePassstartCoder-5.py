
```cpp
#include <iostream>

int a = 3;
int b = 4;
int c = 5;

int main() {
  int result = 0;
  result = (a + b) + c;
  result = (result * a) * b;
  result = (result - c) - a;
  std::cout << result << std::endl;
  return 0;
}
```

