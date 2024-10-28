
```c
#include <stdio.h>

// switch function
int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 1:
      result = x * 32 + 15;
      break;
    case 2:
      result = x - 15;
      break;
    default:
      result = x + 3;
      break;
  }
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 15);
  result = switch_func(a);
  printf("%d\n", result);
  return result;
}
```

