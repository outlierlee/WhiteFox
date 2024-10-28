
```c
#include <stdlib.h>
#include <string.h>

int main() {
    char *buffer = (char *)malloc(100);
    if (!buffer) return -1;

    memset(buffer, 0, 50);
    memset(buffer + 50, 1, 10);
    memset(buffer + 30, 2, 70);

    free(buffer);

    return 0;
}
```

