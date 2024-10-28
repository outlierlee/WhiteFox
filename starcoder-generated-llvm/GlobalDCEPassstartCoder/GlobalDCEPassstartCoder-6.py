
```cpp
#include <iostream>
#include <vector>
#include <string>

static int unused_function() {
  int result = 0;
  bool flag = false;
  float a = 0;
  long some_val = -43;
  if (some_val == 12) {
    result = 123;
  } else {
    if (a == 0.0) {
      result++;
      if (flag == true) {
        result = result + 2;
      }
    }
  }
  return result;
}

int main() {
  int main_result = 0;
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec[2] = 5;
  main_result = vec[2] + str[2] + unused_function();
  return main_result;
}
```

