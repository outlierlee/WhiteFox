
```c
#include <stdlib.h>
#include <string.h>

int main() {
    int *buffer = (int *)malloc(40);
    int value = !buffer ? -1 : 0;

    for (int i = 0; i < 10; ++i) {
        buffer[i] = 1 << i;
    }

    memset(buffer, 0, 40);

    for (int i = 0; i < 10; ++i) {
        buffer[i] += 1;
    }

    free(buffer);

    return value;
}
```

