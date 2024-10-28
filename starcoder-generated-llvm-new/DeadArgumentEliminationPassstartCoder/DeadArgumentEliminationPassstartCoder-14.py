
```c
#include <stdio.h>

int func_with_unused_params(int a, int b, int c) {
  int result;
  sploits[7] = func2(argc, argv);
  result=a+b;
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 31);
  int b = sploits[7] = 24;
  result = func_with_unused_params(a, b, 25);
  return result;
}
```

