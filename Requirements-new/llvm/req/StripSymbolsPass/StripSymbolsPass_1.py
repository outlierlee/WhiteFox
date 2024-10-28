#include <stdio.h>

// Define a struct with a typedef
typedef struct {
    int a;
    float b;
} MyStruct;

// Define a global variable of the typedef struct
MyStruct globalVar = {1, 2.0};

// Define a function that uses the typedef struct
void useStruct(MyStruct *s) {
    printf("a: %d, b: %f\n", s->a, s->b);
}

int main() {
    // Call the function with the global variable
    useStruct(&globalVar);
    return 0;
}
