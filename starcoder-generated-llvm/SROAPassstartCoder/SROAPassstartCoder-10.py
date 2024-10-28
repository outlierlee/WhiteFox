
```c
#include <stdio.h>

typedef struct {
    float a;
    char b;
    double c;
} MyStruct;

void useStruct(MyStruct *s) {
    s->a = 10.0001;
    s->b = 'z';
    s->c = 30.00001;
}

int main() {
    MyStruct s;
    useStruct(&s);
    printf("%f %c %lf\n", s.a, s.b, s.c);
    return 0;
}
```
