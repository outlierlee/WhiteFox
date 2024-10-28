
```c
#include <stdio.h>

typedef struct {
    int a;
    float b;
} MyStruct;

MyStruct globalVar = {1, 2.0};

void useStruct(MyStruct *s) {
    printf("a: %d, b: %f\n", s->a, s->b);
}

int main() {
    useStruct(&globalVar);
    return 0;
}
```

