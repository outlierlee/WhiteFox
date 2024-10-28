
```cpp
#include <stdio.h>

// Define a struct using typedef
typedef struct {
    int a;
    float b;
} MyStruct;

// Define a global variable
MyStruct myStruct = {1, 2.0};

// Define a function that uses the typedef struct
void useStruct(MyStruct* s) {
    printf("a: %d, b: %f\n", s->a, s->b);
}

int main() {
    // Call the function with the struct
    useStruct(&myStruct);
    return 0;
}
```
