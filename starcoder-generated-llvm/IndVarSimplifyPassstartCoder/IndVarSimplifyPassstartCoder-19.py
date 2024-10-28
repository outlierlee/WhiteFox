```c
#include <stdio.h>

int main() {
    int sum = 0;
    int array[5] = {0,1,2,3,4};
    for(int i=0; i<5; i++){
        sum += array[i];
        
    }
    printf("Sum: %d\n", sum); 
    return sum;
}
```
