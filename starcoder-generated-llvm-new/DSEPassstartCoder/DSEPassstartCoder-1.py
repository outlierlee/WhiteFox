```cpp
#include <unistd.h>
#include <stdlib.h>

int main() {
    // Allocate memory
    char *buffer = (char *)malloc(100);
    if (!buffer) return -1;

    // Perform a store operation
    char store_value = 0;
    ssize_t bytes_written = write(STDOUT_FILENO, &store_value, 1);
    if (bytes_written != 1) return -2;

    // Perform another store operation (overwriting the previous one)
    store_value = 1;
    bytes_written = write(STDOUT_FILENO, &store_value, 1);
    if (bytes_written != 1) return -2;

    // Free the allocated memory
    free(buffer);

    return 0;
}
```
