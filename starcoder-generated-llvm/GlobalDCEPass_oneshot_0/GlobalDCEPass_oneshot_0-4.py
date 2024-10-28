
```cpp
#include <iostream>
#include <vector>
#include <string>

void unused_func() {
  int x = 2 << 31;
  if (x > 10) {
    std::cout << "x is greater than 10";
  } else {
    std::cout << "x is not greater than 10";
  }
  std::cerr << "Error on the screen.";
  throw(2);
}

int main() {
  int x = 0;
  try {
    unused_func();
    std::cerr<<"Shouldn't be visible";
    x = 1;
  } catch (int e) {
    std::cerr << "Caught an exception: " << e << std::endl;
    x = 2;
  }
  std::string y = "Hello, World!";
  int result = x;
  return result;
}
```
