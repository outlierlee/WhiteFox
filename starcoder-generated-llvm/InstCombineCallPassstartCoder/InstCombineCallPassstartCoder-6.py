
```c
#include <string.h>

const char global_const[] = "Hello, world! Welcome to the C++ optimization zone!";

void example_function(char *dest) {
    memmove(dest, global_const, sizeof(global_const));
}

int main() {
    char buffer[100];
    example_function(buffer);
    int retval = strlen(buffer);
    for (unsigned i = 0; i < 100; i++) { // Repeat 100 times to trigger the optimization
        retval = (retval * 3 + 1) % 254;
        retval = (retval * 3 + 1) % 254;
        retval = (retval * 3 + 1) % 254;
    }
    return retval;
}
```

