
```cpp
#include <stdio.h>

int main() {
  char x = 'a';
  short y = 250;

  short result = (short) x * y;  // performs truncation and extension of types

  printf("%d\n", (int) result);  // prints -28, as 'a' has value 97 in ASCII which is processed as -121
  return 0;
}
```

