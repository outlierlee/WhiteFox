
```c
#include <stdio.h>

// Define a struct with a typedef
typedef struct {
    int a;
    float b;
} MyStruct;

// Define a global variable of the typedef struct
MyStruct globalVar = {5, 10.0};

// Define a function that uses the typedef struct
void useStruct(MyStruct *s) {
    int res = 1;
    for (int i = 0; i < s->a; i++) {
        res = res + res;
    }
    printf("a: %d, b: %f, res: %d\n", s->a, s->b, res);
}

int main() {
    // Call the function with the global variable
    useStruct(&globalVar);
    return 0;
}
```
