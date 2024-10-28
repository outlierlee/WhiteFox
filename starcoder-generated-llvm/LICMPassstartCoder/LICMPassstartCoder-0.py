
```cpp
#include <vector>
#include <string>
#include <cmath>

int main() {
  int result = 0;
  std::vector<int> vec = {0, 1, 2, 3, 4, 5};

  for (int i = 0; i < 6; i++){
    if (vec[i] % 2 != 0) {
      result += vec[i] * vec[i] - vec[i] - 2;
    } else {
      result += vec[i] * vec[i] + vec[i] + 2;
    }
  }
  
  return result;
}
```

