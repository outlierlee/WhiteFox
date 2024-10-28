
```c
#include <string.h>

const char global_const[] = "Hello, Quality Assurance!";

void example_function(char *dest) {
  memmove(dest, global_const, sizeof(global_const));
}

int main() {
  char buffer[100];
  example_function(buffer);
  return 0;
}
```
