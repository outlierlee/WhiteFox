
```c
#include <stdio.h>

int main() {
    int a, b, c;
    int aa[10], bb[10], cc[10];

    for (a = 0; a < 10; a++) {
        aa[a] = a * 2;
        bb[a] = a * 3;
    }

    for (b = 0; b < 10; b++) {
        aa[b] += b;
    }

    for (c = 0; c < 10; c++) {
        bb[c] += c;
    }

    for (a = 0; a < 10; a++) {
        cc[a] = aa[a] + bb[a];
    }

    for (a = 0; a < 10; a++) {
        printf("%d ", cc[a]);
    }

    return 0;
}
```
