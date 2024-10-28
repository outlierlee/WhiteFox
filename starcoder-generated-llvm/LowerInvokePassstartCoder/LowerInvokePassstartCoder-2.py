
```cpp
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void my_function() {
  if (setjmp(buf)) {
    printf("After longjmp\n");
  } else {
    int a = 120;
    printf("Before longjmp, %d\n", a);
    longjmp(buf, 1);
  }
}

class MyClass {
  public:
    MyClass(const char* msg) : msg_(msg) {}
    ~MyClass() { printf("MyClass destroyed: %s\n", msg_); }

  private:
    const char* msg_;
};

int main() {
  int result = 0;
  MyClass* m = new MyClass("Hello");
  if (setjmp(buf)) {
    printf("After longjmp\n");
    result |= 1;
  } else {
    printf("Before longjmp\n");
    longjmp(buf, 1);
  }
  MyClass m2("World");
  my_function();
  delete m;
  return result;
}
```

