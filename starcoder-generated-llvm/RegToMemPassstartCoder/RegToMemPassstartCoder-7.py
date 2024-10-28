
```c
#include <stdio.h>

void example_function() {
  int vec[5] = {0, 1, 2, 3, 4};
  float vec2[5] = {1.0, 1.5, 2.0, 2.5, 3.0};
  char vec3[5] = {'a', 'b', 'c', 'd', 'e'}; 
  
  // Loop over the arrays and perform operations
  for (int i = 0; i < 5; i++) {
    vec[i] = vec[i] * 2;
    vec2[i] = vec2[i] / 2.0;
    vec3[i] = vec3[i] + 1;
  }

  // Add a conditional based on a value in the array
  if (vec[0] > 5) {
    printf("vec[0] is larger than 5\n");
  }
}

int main() {
  example_function();
  return 0;
}
```
