
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
  int result = 0;

  int a = (1 << 31);
  int b = a;
  if (a != 0) {
    result = a / b;
  } else {
    result = 0;
  }
  int redundant = result * 1;

  std::vector<int> vec = {0, 1, 2, 3};
  vec.assign(4, 1);
  int index = vec.at(1);

  std::string str = "hello";
  str.assign("hello", 3);
  std::cout << "Result: " << result << ", Redundant: " << redundant << std::endl;

  return 0;
}
```
