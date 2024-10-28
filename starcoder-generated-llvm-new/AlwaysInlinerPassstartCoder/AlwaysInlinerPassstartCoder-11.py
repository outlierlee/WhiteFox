
```c
#include <string.h>
#include <stdio.h>

inline int inline_func(int a, int b) {
  return a + b;
}

int cmpfunc (const void * a, const void * b) {
  return ( *(int*)a - *(int*)b );
}

int main() {
  int result = 0;
  int x = 5;
  int y = 10;
  char str[80];

  strcpy(str,"This is string.h library function used here.");
  
  inline_func(x, y);
  
  qsort (str, sizeof(str), sizeof(char), cmpfunc);
  
  result = strlen(str);
  return result;
}
```
