
```cpp
#include <stdio.h>

typedef struct {
    int a;
    float b;
    char c;
    void* d;
} MyStruct;

void useStruct(MyStruct* s) {
    s->a = 10;
    s->b = 20.5;
    s->c = 'z';
    s->d = nullptr;
    s->a = 30;
}

int main() {
    MyStruct s;
    useStruct(&s);

    printf("%d %f %c\n", s.a, s.b, s.c);
    return 0;
}
```
