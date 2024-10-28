
```c
#include <string.h>

const char global_const[] = "Hello, World!";

void example_function(char *dest) {
    memmove(dest, global_const, sizeof(global_const));
}

int main() {
    char buffer[50];
    example_function(buffer);
    return 0;
}
```
