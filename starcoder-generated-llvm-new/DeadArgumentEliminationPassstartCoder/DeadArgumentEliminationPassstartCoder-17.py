
```c
int x = -4225923;
unsigned int y = 6453758; 
int z = 1; 
int func_with_unused_params(int a, int b, int c) {
   int result = 0;
   result = x + a;
   if (result > 0)
     result = result / 2 + 10;
   else 
     result = result - 5;
   return result;
}

int main() {
   int a, b;
   a = 0;
   b = 0;
   int result = func_with_unused_params(a, b, x);
   return result;
}
```
