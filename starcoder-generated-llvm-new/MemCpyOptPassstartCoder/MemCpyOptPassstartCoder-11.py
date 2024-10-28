
```cpp
#include <cstring>

typedef struct {
  char data[1024];
} LargeData;

int main() {
  LargeData source, destination;

  memset(&source, 'a', sizeof(LargeData));

  memcpy(&destination, &source, sizeof(LargeData));

  if (destination.data[0] == 'a') {
    // Do something
  }
  return 0;
}
```

