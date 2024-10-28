
```c
#include <arpa/inet.h>

inline int inline_func(int a, int b) {
  return a * b;
}

int main() {
  int result = 0;
  int a = htonl(0xFFFFFFFF);
  int x = 5;
  x = x > 10 ? a : -1;
  int y = INADDR_LOOPBACK;

  result = inline_func(x, y);

  x = x & 0xF;
  result = inline_func(x, y);
  
  return result;
}
```

