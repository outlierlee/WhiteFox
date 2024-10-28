
```c
#include <stdio.h>

void example_function() {
  long long a = 10;
  unsigned int b = 20;
  float c = 2.0;
  double d = 3.0;
  int e = 4;

  a += 5;
  b -= 1;
  c *= 2.0;
  d /= 2.0;
  e *= 2;

  printf("a: %llu, b: %u, c: %f, d: %f, e: %d\n", a, b, c, d, e);
}

int main() {
  example_function();

  return 0;
}
```

