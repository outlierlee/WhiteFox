
```c
#include <stdio.h>

int varargs_func(int x, int y, int z, int w) {
  if (x % 2) {
    return x * 32 + 15;
  } else {
    return x - 15;
  }
}

int main() {
  int a = (1 << 31);
  int b, c, d, e, f, g, h, i, j, k, l, m, n;
  b = c = d = e = f = g = h = i = j = k = l = m = n = 10;
  int result = varargs_func(a, b, c, d);
  if (result > 100) {
    result = result * 2;
  } else {
    result = result * 2;
  }
  printf("Result: %d\n", result);
  return 0;
}
```

