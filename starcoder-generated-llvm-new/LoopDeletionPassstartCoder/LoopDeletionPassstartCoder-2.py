
```cpp
#include <vector>

int main() {
  std::vector<int> vec = {0, 1, 2, 3};
  vec.assign(5, 42);

  for (int i = 0, j = 0; i < vec.size(); i++) {
    j = vec[i] + j;
  }
  
  int y = vec.size();
  
  return y;
}
```

