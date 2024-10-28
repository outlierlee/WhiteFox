
```cpp
#include <vector>
#include <string>

void __attribute__((noinline)) func(int arg1, int arg2, std::vector<int> arg3, double arg4) {
    int c = arg1 + arg2 * arg3[0] + arg4;
}

int main() {
  int x = ((1 << 31));
  int y = 50;
  std::vector<int> vec = {1, 2, 3};
  double z = 1.000000;

  func(x, y, vec, z);

  return 0;
}
```

