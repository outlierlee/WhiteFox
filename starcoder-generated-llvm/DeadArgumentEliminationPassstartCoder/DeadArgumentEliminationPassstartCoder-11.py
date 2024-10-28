
```c
#include <string.h>

struct {
  int x;
  char y;
} structVar;

int main() {
  int x = 5;
  double y = 3.14;
  struct {
    int x;
    char y[5];
  } structVar;
  char arr[] = "hello";
  const char *str = "world";
  int result = func_with_unused_params(x, y, arr);
  return result;
}

int func_with_unused_params(int a, int b, int c) {
  int result = 0;
  double d;
  if (a > b || b > c) {
    result = a * b - c;
  } else {
    result = a * b + c;
  }
  return result;
}
```

