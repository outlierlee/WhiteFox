
```cpp
#include <string.h>

typedef struct {
    int data[1024];
} LargeData;

int main() {
    LargeData source, destination;

    for (int i = 0; i < sizeof(source.data) / sizeof(source.data[0]); ++i) {
        source.data[i] = i;
    }

    memcpy(&destination, &source, sizeof(LargeData));

    int used = 0;
    for (int i = 0; i < sizeof(destination.data) / sizeof(destination.data[0]); ++i) {
        if (destination.data[i] == i) {
            used = 1;
            break;
        }
    }

    return used;
}
```
