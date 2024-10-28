
```c
#include <stdio.h>

typedef struct {
    char a;
    double b;
    int *c;
} MyStruct;

void useStruct(MyStruct *s) {
    s->a = 'a';
    s->b = 30.0;
    s->c = &(s->a);
}

int main() {
    int x = 30;
    MyStruct s{};
    
    s.c = &x;
    useStruct(&s);

    printf("%c %.2lf %p\n", s.a, s.b, s.c);

    return 0;
}
```
