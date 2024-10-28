
```cpp
#include <iostream>
#include <vector>
#include <string>

static void varargs_func(int x, ...) {
  for (int i = 0; i < x; ++i) {
    int sum = 0;
    for (int j = 0; j < 10; ++j) sum += j;
    std::cout << "Sum: " << sum << std::endl;
  }
}

int main() {
  int x = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  varargs_func(x, 18, 25, vec[1], 1.000000, str[3]); // you can pass the arguments with any number, any type
  return 0;
}
```
