
```c
#include <stdio.h>

void example_complex_function(int a, float b, char c) {
 int d = a + b;
 float e = a * c;
 char f = (d > 'a') ? c : 'b';
 printf("d: %d, e: %f, f: %c\n", d, e, f);
}

int main(){
 int a = '100';
 float b = 19.87;
 char c = 'd';
 example_complex_function(a,b,c);
 return 0;
}
```

