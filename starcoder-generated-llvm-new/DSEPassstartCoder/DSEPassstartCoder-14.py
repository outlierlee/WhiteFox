
```c
#include <stdlib.h>
#include <string.h>

int main() {
    int* buffer = (int*)malloc(sizeof(int)*10);

    if (!buffer) return -1;
    
    int toStore = 17;
    int j;
    for (j = 0; j < 10; j++) {
        buffer[j] = toStore;
    }

    memset(buffer, 0, sizeof(int)*10);

    free(buffer);

    return 0;
}
```
# C Code ends 

