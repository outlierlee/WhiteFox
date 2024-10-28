
```c
#include <stdio.h>

int global_func1(int x) {
  return x * 2;
}

float global_var3 = 2.71;

int main() {
  int i = (1 << 31);
  int result = 0;
  for (int j = 0; j < (1 << 31); ++j) {
    i = i + 50;
    result += global_func1(i - 4) * j;
  }
  return result;
}
```
