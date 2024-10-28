
```c
#include <string.h>

int main() {
  const char const_array[] = "Hello, World!";
  char local_array[20];

  memcpy(local_array, const_array, sizeof(const_array));
  
  int result = 0;
  for (int i = 0; i < 12; i++) {
    result += local_array[i];
  }

  return result / 3;
}
```
