
```c
#include <stdio.h>

// Declare a struct
typedef struct {
    int a;
    int b;
    float c;
} MyStruct;

// Function that uses the struct
void useStruct(MyStruct *s) {
    // Perform operations on the struct fields
    s->a = 20;
    s->b = -10;
    s->c = 33.1416;
}

int main() {
    // Declare a struct variable
    MyStruct s;
    // Call the function that uses the struct
    useStruct(&s);
    // Print the struct fields
    printf("%d %d %f\n", s.a, s.b, s.c);
    return 0;
}
```
