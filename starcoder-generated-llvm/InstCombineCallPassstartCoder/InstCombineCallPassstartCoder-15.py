
```c
#include <string.h>

// Define a global constant variable
const char seed_data[] = "Hello, World!";

// Define a function that uses memmove
void example_function(char *dest) {
    // Use memmove with the global constant as the source
    memmove(dest, seed_data, sizeof(seed_data));
}

int main() {
    char buffer[21]; // Declare a buffer
    example_function(buffer); // Call the function with the buffer
    return 0;
}
```
