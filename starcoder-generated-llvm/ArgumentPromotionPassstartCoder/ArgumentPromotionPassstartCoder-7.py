
```cpp
#include <stdio.h>

int func(int, int, int, int, int, int, int, int, void*, float*, double*);
static void pointer_func(void*, void(), void*, void(), void*, void(), void*, void(), void*);

int main() {
    int x = 10;
    float y = 5.5f;
    double z = 20.0;

    pointer_func(&x, &y, &z); // correct
    printf("x: %d, y: %.2f, z: %.2f\n", x, y, z);

    return x + y + z;  // correct
}

static void pointer_func(void* a, void(), void(), void(*b)(void), void(), void*, void*, void(), void*) {
  if (a) *((int(*)[])0) = *((int(*)[])0) + 1;
  if (b) ((void(*)())b)();  // do not optimize as 'void()' is void function pointer without parameters
  if (a) (**a.*)a += 2;
}

```
