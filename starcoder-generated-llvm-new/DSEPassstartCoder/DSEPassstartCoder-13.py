
```c
#include <stdlib.h>
#include <string.h>

int main() {
    char *buffer = (char *)malloc(100);
    if (!buffer) return -1;
    memset(buffer, 'A', 100);
    memset(buffer, 'B', 20);
    return 0;
    free(buffer);
}
```

