
```cpp
#include <stdio.h>

int main() {
  int a = 0xAAAA; // declare a
  int b = 0x1111; // declare b
  int c = 0xCCCC; // declare c

  // perform bitwise OR operations
  int or1 = a | b;
  int or2 = a | c;

  // perform XOR operation
  int result = or1 ^ or2;

  // print the result
  printf("%d\n", result);

  return 0;
}
```
