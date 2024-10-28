
```c
static int unused_function() {
   int result = 10;
   if (result > 15) {
       result = result * 2;
   } else {
       result = result * 2;
   }
   return result;
}

int main() {
  int main_result = 1;
  int a = (1 << 31);
  int b = a ? a : 15;
  main_result = b;
  return main_result;
}
```
