
```c
#include <string.h>

int main() {
  const char* str = "Hello, world";
  char buffer[100];
  int pos = -1;

  while (str[++pos] != ',') {
    buffer[pos] = str[pos];
  }
  
  int result = 0;
  for (int i = 0; i <= pos; i++) {
    result += buffer[i];
  }

  return result;
}
```

