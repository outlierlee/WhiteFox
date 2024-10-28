
```cpp
#include <iostream>
#include <vector>

int even_odd_func(int a, int b) {
  if (!(a % 2)) {
    return b * 2;
  } else {
    return b * 3;
  }
}

int main() {
  int a = 10;
  int b = 5;
  std::vector<int> vec = {0, 1, 2, 3};
  int result = 0;
 
  for (int i = 0; i < 10; i++) {
    if (i < 5) {
      result = even_odd_func(a, b);
    } else {
      result = even_odd_func(b, a);
    }
  }

  // Use the result in a conditional branch
  if (result > 20) {
    std::cout << "Result is greater than 20";
  } else {
    std::cout << "Result is 20 or less";
  }

  return 0;
}
```
