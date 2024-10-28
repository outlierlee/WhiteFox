
```c
#include <stdio.h>
#include <string.h>

int func_with_unused_params(int a, int b, int c) {
  int result = 0;
  int array[5] = {2, 0, 500, -987, 23};
  int i, j;
  char str[100] = "Hello";
  for (i = 0; i < 8; i++) {
    for (j = 0; j < 16; j++) {
        str[i] = str[i] * j * array[j % 5];
    }
  }

  result = 5 * array[i % 5] - str[j] * i % j + 3 * i * 50;
  return result;
}

int main() {
  int x = -12345, y = 11, z = 77;
  int main_result = func_with_unused_params(x, y, z);
  return main_result;
}
```
