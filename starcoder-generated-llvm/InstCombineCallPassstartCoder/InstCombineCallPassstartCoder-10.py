
```c
#include <stdio.h>
#include <string.h>

const char global_const[] = "The lazy dog jumps over the quick brown fox!";

void example_function(char *dest) {
    memmove(dest, global_const, sizeof(global_const));
}

int main() {
    char buffer[50] = {0};
    example_function(buffer);
    printf("%s\n", buffer); // Outputs "The lazy dog jumps over the quick brown fox!"
    return 0;
}
```
