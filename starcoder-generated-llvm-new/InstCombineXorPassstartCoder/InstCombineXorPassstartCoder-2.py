
```cpp
#include <stdio.h>

// declare variables
int a = (1 << 31);
int b = -100;
unsigned int c = 200U;
unsigned int d = 350U;

int main() {
  // perform bitwise OR operations
  int or1 = a | b;
  int or2 = a | (int)c;

  // perform XOR operation
  int result = or1 ^ or2;

  // print the result
  printf("%d\n", result);

  return 0;
}
```

