
```cpp
#include <vector>
#include <string>

static int unused_function() {
  int result = 0;
  result = 10;
  return result; 
}

int main() {
  int main_result = 0;
  int a = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(6, 42);

  RANDOM_CODE: // Do something here, but do not call unused_function

  main_result = a;
  return main_result;
}
```
