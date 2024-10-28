
```c
#include <stdio.h>

static int my_function(int a, int b){
  int result = 0;
  if(a){
    result = a / b;
  }
  else{
    result = b / a;
  }
  return result;
}

int main(){
  int a = 100;
  int b = 5;
  int main_result = 0;
  
  main_result = my_function(a, b);
  
  return main_result;
}
```

