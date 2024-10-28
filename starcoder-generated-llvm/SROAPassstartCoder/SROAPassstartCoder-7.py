
```c
#include <stdio.h>

typedef struct {
    int a;
    double b;
    char* c;
} StaticAlloc;

void useStatic(StaticAlloc *obj, int size) {
    size *= 5;
    printf("%d %lf %s\n", obj->a, obj->b, obj->c);
}

int main() {
    StaticAlloc obj = { 1, 3.2, "hey" };
    useStatic(&obj, sizeof obj);
    return 0;
}
```

