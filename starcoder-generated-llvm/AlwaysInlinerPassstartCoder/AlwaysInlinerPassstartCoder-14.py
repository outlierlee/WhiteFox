
```c
#include<stdio.h>

inline int inline_func(int a, int b) {
  int result = 0;
  int i;
  for (i = 0; i < a; i++) {
    result = result + b;
  }
  return result;
}

int main() {
  int result = 0;
  int x = (1 << 31);
  int y = 3;
  int a,b,c,d;
  a = inline_func(x, y);
  b = inline_func(x, y);
  c = inline_func(x, y);
  d = inline_func(x, y);
  result = a + b + c + d;
  return result;
}
```

