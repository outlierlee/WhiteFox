
```c
extern "C" {

// This funciton is placed into the text segment to simulate a global function
static int my_function(int a, int b) {
  int result = 100;
  if (a != 0) {
    result = a * a + 3;
  } else {
    result = b * b + 3;
  }
  if (result > 1000) {
    result = result + 500;
  } else {
    result = result * 3;
  }
  return result;
}

int main() {
  int a = (1 << 16);
  int b = (1 << 15);
  int result = 0;
  result = my_function(a, b);
  return result;
}

} // Extern "C"
```
