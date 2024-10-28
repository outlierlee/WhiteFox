
```cpp
#include<stdio.h>

void loop_with_condition(int n, int i, int flag) {
    for (int j = i; j < n; ++j) {
        if (flag) {
            printf("Flag is true, iteration %d\n", j);
        } else {
            printf("Flag is false, iteration %d\n", j);
        }
    }
}

int main() {
    int n = 10;
    int i = 0;
    int flag = -1;

    while(i < n) {
        if(flag) {
            loop_with_condition(n, i, 1);
        } else {
            loop_with_condition(n, i, 0);
        }
        i += (n+flag);
    }
    return 0;
}
```

