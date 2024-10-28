
```cpp
#include <stdio.h>

int x = -1;
struct SomeStruct {
  int a;
  char b;
};

int main() {
  SomeStruct someStruct = {.a = 50, .b = 'S'};
  long long longValue = 564092657159168L;
  float floatValue = longValue;
  int result = (int) --(floatValue - someStruct.a); // Note the expression involves pre- and post-decrement
  printf("%d\n", result);
  return 0;
}
```
