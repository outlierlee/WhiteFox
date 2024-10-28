
```cpp
#include <vector>
#include <string>

int no_side_effect_func(int x) {
  if (x % 2) {
    return x * 32 + 15;
  } else {
    return x - 15;
  }
}

int main() {
  int result = 0;
  int a = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  for (int i = 0; i < a; ++i) {
    int x = vec[i];
    result = no_side_effect_func(x);
    if (result > 20) {
      result = 1;
    } else if (result < 15) {
      result = 0;
    } else {
      result = vec[4] + 1;
    }
  }
  return result;
}
```

