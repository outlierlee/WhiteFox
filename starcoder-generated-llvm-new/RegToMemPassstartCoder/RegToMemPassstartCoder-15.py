
```c
#include <stdio.h>

int varargs_func(int a[], int size) {
  int result = a[0];
  for(int i = 1; i < size; ++i) {
    result += a[i];
  }
  
  if (result > 10) {
    result = result * 2;
  } else {
    result = result / 2;
  }
  
  return result;
}

int main() {
  int a[3];
  a[0] = 2;
  a[1] = 3;
  a[2] = 7;
  int result = varargs_func(a, 3);
  printf("varargs_func result: %d\n", result);
  return 0;
}
```

