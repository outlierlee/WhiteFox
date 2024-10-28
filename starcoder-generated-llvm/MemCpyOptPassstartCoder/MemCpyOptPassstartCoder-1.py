```cpp
#include <cstring>

typedef struct {
  char data[4096];
} LargeData; // this <<4096>> value is significant enough to optimize

int main() {
  LargeData source, destination;

  std::memset(&source, 1, sizeof(LargeData)); //value 1 can't be replaced with bad value

  std::memcpy(&destination, &source, sizeof(LargeData));

  if (destination.data[0] == 1) {
    for(int i = 0; i < 4096; ++i) {
      if (destination.data[i] == 1) {
        continue;
      } else {
        return -1; // or throw an exception because this should not happen
      }
    }
  }

  return 0;
}
```
