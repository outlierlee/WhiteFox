
```cpp
#include <cstddef>
#include <iostream>
#include <vector>
#include <string>

int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 1:
      result = x + 1;
      break;
    case 2:
      result = x + 2;
      break;
    default:
      result = x + 3;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = 1;
  std::vector<int> vec(5, 1);
  main_result = switch_func(vec[0]);
  printf("%d\n", main_result);
  std::string str = "hello";
  std::string subString = str.substr(2, 2);
  vec.assign(10, 3);
  vec.push_back(5);
  main_result = switch_func(vec.at(5));
  printf("%d\n", main_result);
  return main_result;
}
```
