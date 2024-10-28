
```c
#include <stdlib.h>
#include <string.h>

int main() {
    // Allocate memory
    char *buffer = (char *)malloc(100);
    if (!buffer) return -1;

    // Perform a store operation
    memset(buffer, 0, 100);

    // Perform another store operation that overwrites the previous one
    memset(buffer, 1, 100);

    // Free the allocated memory
    free(buffer);

    return 0;
}
```
