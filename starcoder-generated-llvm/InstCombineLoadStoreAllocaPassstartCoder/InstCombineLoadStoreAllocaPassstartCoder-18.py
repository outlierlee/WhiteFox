
```cpp
#include <string.h>

int main() {
  const char const_array[] = {'H', 'e', 'l', 'l', 'o', '\0'};
  char local_array[10];
  memcpy(local_array, const_array, sizeof(const_array));
  int result = local_array[0] + local_array[1];
  return result;
}
```

