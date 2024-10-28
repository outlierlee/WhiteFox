
```cpp
#include <stdio.h>

int main() {
  float a = 32.100000;
  float b = 56.900002;
  float c = 88.100002;
  float result;

  if (a > b) {
    result = a;
  } else {
    result = b;
  }

  result = (a > b) ? a : b;

  printf("Result: %f\n", result);

  return 0;
}
```
# C++ code ends