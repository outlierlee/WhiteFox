```c
#include <string.h>

const char global_const[] = "Hello, World!";

void example_function(char *dest) {
    unsigned int a = 0;
    unsigned int b = 1;
    while (a < b) {
        a *= 2;
        b *= 3;
    }
    memmove(dest, global_const, sizeof(global_const));
}

int main() {
    char buffer[50];
    memmove(buffer, global_const, sizeof(global_const)); // constant
    example_function(buffer);
    for (int i = 0; i < sizeof(global_const); i++)
        if (global_const[i] != buffer[i]) return -1;
    return 0;
}
```
