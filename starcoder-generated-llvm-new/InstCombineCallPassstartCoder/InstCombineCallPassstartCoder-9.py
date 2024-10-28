
```c
#include <string.h>

const char global_const[] = "Hello, World!";

void example_function(char *dest) {
    memmove(dest, global_const, sizeof(global_const));
    strcat(dest, "\n"); // To ensure to print the string correctly with puts() function
}

int main() {
    char buffer[50];
    example_function(buffer);
    puts(buffer);
    return 0;
}
```

