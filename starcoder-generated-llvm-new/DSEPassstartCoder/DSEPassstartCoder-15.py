
```cpp
#include <cstdlib>
#include <cstring>

int main() {
  // Allocate memory
  char* buffer = new char[100];
  if (!buffer) return -1;

  // Perform a store operation
  memset(buffer, 0, 100);

  // Perform another store operation that overwrites the previous one
  memset(buffer, 1, 100);

  // Free the allocated memory
  delete[] buffer;
  
  return 0;
}
```

