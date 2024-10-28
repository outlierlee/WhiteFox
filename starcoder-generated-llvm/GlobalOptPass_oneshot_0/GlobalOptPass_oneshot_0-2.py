
```cpp
#include <vector>
#include <string>

void __attribute__((noinline)) func(int arg1, char arg2) {
  arg1 *= 2;
  arg2 += 1;
}

int main() {
  int a = (1 << 15);
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  func(a, str[3]);
  return 0;
}
```

