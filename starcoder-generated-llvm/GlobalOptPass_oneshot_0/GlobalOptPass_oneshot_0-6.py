
```cpp
#include <iostream>
#include <vector>
#include <string>

void __attribute__((noinline)) func(int arg1, float arg2, const std::string& str) {
  if (arg1 < arg2) {
    std::cout << "Argu1 is less than arg2\n";
  } else {
    std::cout << "Argu1 is not less than arg2\n";
  }
}

int main() {
  int x = 10;
  float y = 20.5;
  std::string str = "hello world";

  func(x, y, str);
  return 0;
}
```

