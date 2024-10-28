
```c
#include <stdio.h>

typedef struct {
    int a;
    float b;
} MyStruct;

MyStruct globalVar = {323, 32.3};

void useStruct(MyStruct *s) {
    float c = s->b;
    for (int i = 0; i < s->a; i++) {
        printf("%f\n", c - globalVar.b);
    }
}

int main() {
    useStruct(&globalVar);
    return 0;
}
```
