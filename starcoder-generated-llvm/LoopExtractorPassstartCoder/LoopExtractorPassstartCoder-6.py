
```cpp
#include <iostream>
#include <vector>
#include <string>

void loop_function() {
  int j, sum = 0;

  for (j = 0; j < 100; j++) {
    sum += j;
  }
  
  for (j = 1000; j <= 1100; j++) {
    sum += j;
  }

  std::cout << "Sum: " << sum << std::endl;
}

int main() {
  loop_function();

  return 0;
}
```
