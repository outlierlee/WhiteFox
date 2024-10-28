#include <string.h>

// Define a global constant variable
const char global_const[] = "Hello, World!";

// Define a function that uses memmove
void example_function(char *dest) {
    // Use memmove with the global constant as the source
    memmove(dest, global_const, sizeof(global_const));
}

int main() {
    char buffer[50]; // Declare a buffer
    example_function(buffer); // Call the function with the buffer
    return 0;
}
