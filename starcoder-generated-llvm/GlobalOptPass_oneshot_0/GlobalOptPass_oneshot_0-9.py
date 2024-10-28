
```cpp
#include <vector>
#include <string>

typedef int (*Func)(...);
Func globalFunc;

extern "C" void __attribute__((fastcc, noinline)) func(int x, int y, int z, double d, char c) {
  int result = 0;
  int sum = (x + y + z);
  if (sum % 2 && d > 5.5 && c != 0) {
    result = sum * 32 + 15;
  } else {
    result = sum - 15;
  }
  if (sum > 100) {
    result = result * 2;
  } else {
    result = result * 4;
  }
  globalFunc = nullptr;
}

int main() {
  int a = (1 << 31);
  int b = 0;
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  globalFunc = func;
  globalFunc(a, vec[1], 1.000000, vec[1], str[3]);
  b = a;
  return b;
}
```

