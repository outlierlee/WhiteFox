
```c
#include <stdio.h>

// Define a struct with an enum in it
typedef enum {SUCCESS, FAILURE} Result;
typedef struct {
    int a;
    Result res;
} MyStruct;

// Define a global variable of the typedef struct
MyStruct globalVar = {1, SUCCESS};

// Define a constant variable of the typedef struct
const MyStruct constVar = {0, FAILURE};

// Define a function that uses the typedef struct
void useStruct(MyStruct *s) {
    printf("a: %d, res: %d\n", s->a, s->res);
}

int main(){
    // Call the function with both the global and constant variables
    useStruct(&globalVar);
    useStruct(&constVar);
    return 0;
}
```

