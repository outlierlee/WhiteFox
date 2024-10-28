
```c
#include <stdio.h>

#define N 5

char buff[N];
char* const upStream = &buff[0];
char* pntr = &buff[N/2];
char* limt = &buff[N];

void int_arithematic(int x) {
    *pntr++ = x;
}

void int_operation(){
    while (pntr < limt){
        int a = *upStream++;
        int b = *upStream++;
        if ((a&32)) {
            int_arithematic(a*32 + b + 15);
        } else {
            int_arithematic(a - b);
        }
    }
}

int main() {
    char* topStream = upStream;
    int_operation();

    printf("%d\n", buff[0]);
    printf("%d\n", buff[1]);
    printf("%d\n", buff[2]);
    printf("%d\n", buff[3]);
    printf("%d\n", buff[4]);

    return 0;
}
```
I have added a function `int_arithematic` to initiate the values in the array and another function `int_operation` to perform the conditional operations inside conditional blocks.

