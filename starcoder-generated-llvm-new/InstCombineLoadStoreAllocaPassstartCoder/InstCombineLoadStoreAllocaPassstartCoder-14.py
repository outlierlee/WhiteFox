
```c
#include <string.h>

int main() {
  const int const_array[] = {100, 200, 300, 400, 500};
  int local_array[5];
  memcpy(local_array, const_array, sizeof(const_array));
  for (int i = 0; i < 5; i++) {
    local_array[i] += 150;
  }
  int result = local_array[0] + local_array[1];
  return result;
}
```
# C Code ends