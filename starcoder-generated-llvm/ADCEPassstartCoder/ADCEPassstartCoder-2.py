
```cpp
#include <iostream>
#include <vector>

int compute(int x, int y) {
  int result = x + y;
  return result;
}

int main() {
  const int SIZE = 10;
  std::vector<int> vec(SIZE, 1);
  
  int a = vec[0];
  int b = vec[1];
  
  for (int i = 2; i < SIZE; i++) {
    vec[i] = 0;
  }

  int main_result = compute(a, b);

  std::cout << "Result: " << main_result << std::endl;

  return main_result;
}
```

