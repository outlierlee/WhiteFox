
```c
#include <stdlib.h>
#include <string.h>

int main() {
    char *buffer = (char *)malloc(100);
    if (!buffer) return -1;

    memset(buffer, 5, 100); 

    memset(buffer, 1, 50);

    free(buffer);

    return 0;
}
```

