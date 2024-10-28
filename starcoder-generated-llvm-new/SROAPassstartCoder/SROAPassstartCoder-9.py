
```c
#include <stdio.h>

// Define a struct with multiple fields
typedef struct {
    int a;
    float b;
    char c;
} MyStruct;

// Function that uses the struct
void useStruct(MyStruct *s) {
    // Perform operations on the struct fields
    s->a = 99;
    s->b = 25.0;
    s->c = 'y';
}

int main() {
    // Declare a struct variable
    MyStruct s;

    // Call the function that uses the struct
    useStruct(&s);

    // Print the struct fields
    printf("%d %f %c\n", s.a, s.b, s.c);

    return 0;
}
```

