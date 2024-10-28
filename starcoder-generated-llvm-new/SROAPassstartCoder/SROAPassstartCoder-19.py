```c
#include <stdio.h>

typedef struct {
    int a;
    float b;
    float c;
} MyStruct;

void useStruct(MyStruct *s) {
    s->a = 10;
    s->b = 20.5;
    s->c = 12.5;
}

int main() {
    MyStruct s = {0};
    useStruct(&s);
    printf("%d %f %f\n", s.a, s.b, s.c);
    return 0;
}
```

# C Code ends

Please use the following data in defining the variables:

```
a = 2147483647 
b = 1.5 
c = 69 
```

If the C code can be optimized, it should be optimized. Otherwise, the resulting assembly code should follow certain patterns.