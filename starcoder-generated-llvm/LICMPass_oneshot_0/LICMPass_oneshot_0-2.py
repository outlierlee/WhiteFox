
```cpp
#include <vector>
#include <string>

int no_side_effect_func(int x) {
  int result = 10;
  if (x % 2) {
    result = x * 32 + 15;
  } else {
    result = x - 15;
  }
  if (x > 100) {
    result = result * 2;
  } else {
    result = result * 2;
  }
  return result;
}

int main() {
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  for (int i = 0; i < 1000; ++i) {
    if (1 == vec[i%vec.size()] || 
        'h' == str[i%str.size()] || 
        2 == no_side_effect_func(i)) {
      // do something
    }
  }
  return 0;
}
```
