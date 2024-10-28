
```cpp
#include<stdio.h>

int main() {
  unsigned int x = 4294967295; //2^32-1
  char y = -128;
  int result = (int) (x - y);
  printf("%d\n", result);
  return 0;
}
```
