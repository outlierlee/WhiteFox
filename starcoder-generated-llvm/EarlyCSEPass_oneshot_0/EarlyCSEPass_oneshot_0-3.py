
```cpp
#include <vector>
#include <string>

int main() {
  int x = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  int y = varargs_func(x, 18, 25, vec[1], 1.000000, str[3]);
  int z = y * 2;
  return z;
}
```

