
```c
#include <string.h>

const char global_const[] = "Hello, world! This is a string that is used to demonstrate the optimization. This string is way longer than usual and will be a showstopper for IR Generation!";

void example_function(char *dest) {
    memmove(dest, global_const, sizeof(global_const));
}

int main() {
    char buffer[50];
    example_function(buffer);
    // Print the buffer
    printf("%s", buffer);
    return 0;
}
```
