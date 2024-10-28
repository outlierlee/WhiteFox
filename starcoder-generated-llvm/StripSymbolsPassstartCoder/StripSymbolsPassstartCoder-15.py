
```c
#include <stdio.h>

typedef struct {
    int a;
    double b;
} MyStruct;

MyStruct globalVar = {1, 3.1415926};

void useStruct(MyStruct *s) {
    printf("a: %d, b: %f\n", s->a, s->b);
}

int main() {
    useStruct(&globalVar);
    return 0;
}
```
