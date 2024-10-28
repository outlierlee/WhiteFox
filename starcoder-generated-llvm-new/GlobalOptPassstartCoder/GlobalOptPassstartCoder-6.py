
```cpp
#include <iostream>
#include <vector>
#include <string>

static int my_function(int a, int b) {
  int result = 0;
  if (a % 2) {
      result = a + b;
  } else {
      result = a - b;
  }
  if (a > b) {
      result = result * 2;
  } else {
      result = result / 2;
  }
  return result;
}

int main() {
  int result = 0;
  int x = -1234;
  int y = 5678;

  result = my_function(x, y);
  
  std::vector<int> vec(10, 0);
  vec[9] = result;
  
  x = vec[9];
  y = vec[9];

  return result;
}
```
