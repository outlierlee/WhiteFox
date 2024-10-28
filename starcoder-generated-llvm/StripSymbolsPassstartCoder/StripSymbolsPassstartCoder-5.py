
```c
#include <stdio.h>

// Define a struct with a typedef
typedef struct {
    int a;
    float b;
} MyStruct;

// Define a global variable of the typedef struct
MyStruct globalVar = {1, 2.0};

// Global scope declaration of function that uses the typedef struct
static void useStruct(MyStruct *s) {
    printf("a: %d, b: %f\n", s->a, s->b);
}

int main() {
    // Call the function with the global variable utilized by the statically linked function 'useStruct'
    useStruct(&globalVar);
    
    int a = globalVar.a * 3;
    int b = a + 5;
    
    return b;
}
```

