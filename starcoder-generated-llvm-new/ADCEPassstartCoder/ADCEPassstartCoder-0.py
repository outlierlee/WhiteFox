
```cpp
#include <vector>
#include <string>

int compute(int x, int y) {
  int result = x + y;
  return result;
}

int main() {
  int main_result = 0;
  int a = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  int b = compute(a, 18);

   main_result = b;

  return main_result;
}
```

