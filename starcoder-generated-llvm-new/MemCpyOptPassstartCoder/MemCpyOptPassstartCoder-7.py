
```c
#include <string.h>

#define SIZE 4096
#define VALUE 'a'

typedef struct {
  char data[SIZE];
} LargeData;

int main() {
  LargeData source, destination;

  memset(&source, VALUE, sizeof(LargeData));
  memcpy(&destination, &source, sizeof(LargeData));

  if (destination.data[0] == VALUE) {
    // Do something
  }

  return 0;
}
```

