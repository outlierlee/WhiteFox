#include <stdio.h>

// Define a destructor function
void __attribute__((destructor)) my_destructor() {
    // RANDOM_CODE: Any code that does not affect the global destructors
    printf("Destructor called\n");
}

// Define another destructor function with a different priority
void __attribute__((destructor(101))) another_destructor() {
    // RANDOM_CODE: Any code that does not affect the global destructors
    printf("Another destructor called\n");
}

int main() {
    // RANDOM_CODE: Any code that does not affect the global destructors
    printf("Main function\n");
    return 0;
}
