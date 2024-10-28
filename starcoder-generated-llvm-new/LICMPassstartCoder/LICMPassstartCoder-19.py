```c
#include <stdio.h>

int main() {
    int result = 0;
    int array[10][10];
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            array[i][j] = 5;
        }
    }
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            if ((i + j) % 2 == 0){
                result += array[i][j];
            }
        }
    }
    return result;
}
```
