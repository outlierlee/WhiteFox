
```c
#include <string.h>

int main() {
  const int const_array[] = {14, 13, 77, 88, 99};
  int local_array[5];
  memcpy(local_array, const_array, sizeof(const_array));
  int result = local_array[2] + 1;
  return result;
}
```

