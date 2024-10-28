
```c
#include <stddef.h>
#include <string.h>

const char global_const[] = "Hello, World!";

void example_function(char *dest) {
    memmove(dest, global_const, sizeof(global_const));
}

int main() {
    char buffer[50];
    example_function(buffer);
    return strlen(buffer); // Use strlen instead of return 0 for main function to have return value
}
```

