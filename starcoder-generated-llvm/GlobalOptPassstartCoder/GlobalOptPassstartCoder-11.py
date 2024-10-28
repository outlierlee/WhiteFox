
```cpp
#include <iostream>
#include <vector>
#include <cstdarg>
#include <complex>

static int my_function(int a, int b) {
  if (a < b || a == b) {
    return a * b;
  } else {
    return a / b;
  }
}

int main() {
  std::vector<int> vec({0,1,2,3,4,5,6,7,8,9});
  std::string str = "hello world";
  vec.assign(5, 42);
  int rv = abs(my_function(str[vec[2]], str[vec[3]]));
  vec.clear();
  return rv;
}
```
