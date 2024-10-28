
```cpp
#include <vector>

int no_side_effect_func(int x) {
  int result = 0;
  result = x * 32;
  return result;
}

int main() {
  std::vector<int> vec;
  int loop_trials = 10;
  int result = 0;
  for (int i = 0; i < loop_trials; ++i) {
    int a = vec[0];
    int b = no_side_effect_func(a);
    result = b;
    if (b > 100) {
      result = 0;
    }
  }
  return result;
}
```

