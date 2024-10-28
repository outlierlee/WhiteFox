
```c
#include <stdio.h>

inline char inline_func(char a, char b) {
  return (a + b) / 2;
}

int main() {
  int result = 0;
  char x = 'a';
  char y = 'b';

  result = inline_func(x, y);

  return result;
}
```
