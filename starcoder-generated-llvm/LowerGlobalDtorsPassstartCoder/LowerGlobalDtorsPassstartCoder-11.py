
```c
#include <stdio.h>

void __attribute__((destructor(102))) first_destructor() {
    char c = 'a';
    printf("%d\n", 102 % c);
}

void __attribute__((destructor(101))) second_destructor() {
    short s = 500;
    static short c;
    static short array[5];
    for (c = s; c > 0; c--) {
        array[c%5] += c;
    }
    printf("%d\n", array[2]);
}

void __attribute__((destructor(100))) third_destructor() {
    int array[2] = {1, 2};
    array[1] += array[0];
    static int i = 100;
    for (;i > 0; i--) {
        array[i%2] += i;
    }
    printf("%d\n", array[1]);
}

int main() {
    int a[2] = {1, 2};
    a[1] += a[0];
    int i = 100;
    for (;i > 0; i--) {
        a[i%2] += i;
    }
    printf("%d\n", a[1]);
   return 0;
}
```
