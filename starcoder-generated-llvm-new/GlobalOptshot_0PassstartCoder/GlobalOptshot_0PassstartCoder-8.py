
```c
#include <stdio.h>
#include <string.h>

static int my_function(char str[]) {
  return strlen(str);
}

int main() {
  int result = 0;
  char str[] = "hello";
  result = my_function(str);
  return result;
}
```
