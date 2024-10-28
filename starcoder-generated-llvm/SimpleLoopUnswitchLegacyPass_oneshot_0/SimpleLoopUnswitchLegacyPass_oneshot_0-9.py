
```cpp
#include <vector>

void loop_func(int x) {
  int result = 0;
  for (int i = 0; i < x; ++i) {
    if (i%3 == 0) {
      result = result * 4 + 5;
    } else {
      result -= 10;
    }
  }
}

int main() {
  std::vector<int> vec = {0, 1, 2, 3};
  int a = vec[3] + 5;
  loop_func(a);
  int result = 0;
  return result;
}
```

