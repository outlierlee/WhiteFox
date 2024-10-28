
```c
#include <stdio.h>

typedef struct {
    int a;
    float b;
    char c;
} MyStruct;

void useStruct(MyStruct *s) {
    int i = 10;
    s->a = i;
    float f = 20.5;
    s->b = f;
    char ch = 'z';
    s->c = ch;
}

int main() {
    MyStruct s;
    useStruct(&s);
    printf("%d %f %c\n", s.a, s.b, s.c);
    return 0;
}
```

