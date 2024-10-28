
```c
#include <stdio.h>

typedef struct {
    int a;
    double b;
    char* c;
} MyStruct;

void useStruct(MyStruct *s) {
    s->a = 32;
    s->b = 1298719238912067987;
    s->c = "Hello, world!";
}

int main() {
    MyStruct s;
    useStruct(&s);
    printf("%d %f %s\n", s.a, s.b, s.c);
    return 0;
}
```
