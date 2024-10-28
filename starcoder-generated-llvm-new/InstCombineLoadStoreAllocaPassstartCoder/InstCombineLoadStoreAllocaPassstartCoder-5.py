
```c
#include <string.h>

int main() {
  const char const_string[] = "Hello, World!";
  char local_string[sizeof(const_string)];
  memcpy(local_string, const_string, sizeof(const_string));
  char result = local_string[7];
  return result;
}
```
