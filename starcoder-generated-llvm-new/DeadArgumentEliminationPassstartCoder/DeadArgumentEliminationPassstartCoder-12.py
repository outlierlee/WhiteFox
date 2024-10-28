```c
#include <stdio.h>

int x = 'u';
unsigned char y = 'p';
char* z = "Hello";

int func_with_unused_params(int a, int b, int c) {
  int result = 0;
  int cnt = 0;
  while(cnt < 5) {
    if(cnt > 2) {
      result += y;
    } else {
      result += x;
    }
    cnt++;
  }
  return result;
}

int main() {
  int main_result = 0;
  int a[] = {7, 2, 1, 0, 5};
  z[1] = (char)&func_with_unused_params;
  main_result |= main_result;
  main_result = func_with_unused_params(x, y, a[4]);
  if(main_result != 'p') {
    z[0] = z[2] = '<';
  }
  return z[1] - z[0]; // return the result
}
```
