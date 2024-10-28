
```c
#include <string.h>

int main() {
  const int const_array[] = {1, 2, 3, 4, 5};

  int local_array[5];

  memcpy(local_array, const_array, sizeof(const_array));

  int result = local_array[0] + local_array[1];

  return result;
}
```

