
```cpp
#include <stdio.h>
#include <algorithm>

int x = RAND_INT();
int y = RAND_INT();

int main() {
  int main_result = 0;

  int unused_var = x + y; // Unused variable

  main_result = std::max(x, 42) - std::min(y, 0); // Some operation on x and y that doesn't affect unused_var

  printf("%d\n", main_result); // Printing the result to ensure side effects

  return main_result; // Returning the result
}
```
