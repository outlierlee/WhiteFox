
```c
#include <string.h>

int main() {
  const int const_array[] = {1, -1, 1, -1, 1};
  int local_array[5];
  memcpy(local_array, const_array, sizeof(const_array));
  int result = 0;
  for (int i = 0; i < 5; i++) {
    result += local_array[i];
  }
  return result;
}
```
