
```c
#include <stdio.h>

typedef struct {
    int a;
    float b;
    char c;
} MyStruct;

// Defined a global MyStruct for demonstration.
MyStruct global_s;

void useStruct(MyStruct *s) {
    int x = s->a;
    if (x % 2 == 0) {
        s->a = s->a * 3;
    } else {
        s->a = s->a + 1;
    }

    if (x > 20) {
        s->b = s->b * 1.2;
    } else {
        s->b = s->b - 0.1;
    }

    if (x > 200) {
        s->c = 'A';
    } else {
        s->c = 'B';
    }
}

int main() {
    MyStruct s;
    global_s = s;
    s.a = (1 << 31);
    s.b = 10.2;
    s.c = 'a';
    useStruct(&s);
    printf("%d %f %c\n", s.a, s.b, s.c);
    return 0;
}
```

