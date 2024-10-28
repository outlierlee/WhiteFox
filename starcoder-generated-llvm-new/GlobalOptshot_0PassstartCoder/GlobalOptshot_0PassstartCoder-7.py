
```cpp
#include <string.h>

static int func(int a, int b, int c, int d, char e, char f) {
  int res = a / 2 + b /3 * 10 + c;
  if(res > d && strcmp(&e, &f)) {
    res = a + e * b - f;
  } 
  else{
    res = d;
  } 
  return a + b + c + d;
}

int main() {
  int result = 0;
  result = func(4, 5, 6, 7, 'A', 'B');
  return result;
}
```
