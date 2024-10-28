
```c
#include <stdio.h>

int main() {
    unsigned a = 5;
    unsigned b = 10;
    unsigned c = 5; // Same value as 'a' to trigger common subexpression elimination
    unsigned result1 = 0;
    unsigned result2 = 0;
  
    // Perform operations that can be simplified
    result1 = a * b;  // First computation
    result2 = c * b;  // Second computation, same as result1

    // Print results when value multiplication exceeds 0
    if(result1 >> 1 & 1){
      printf("result1: %u \n", result1);
    }
    if(result2 >> 1 & 1){
      printf("result2: %u \n", result2);
    }  

    return 0;
}
```
