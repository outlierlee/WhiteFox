```cpp
#include <unistd.h>

static int varargs_func(int argc, ...) {
    if (argc > 0) {
        int res = read(0, NULL, argc);
        if (res == -1) {
            _exit(1);
        }
    }
    return argc + 1;
}

int main(int argc, char** argv) {
    int result = varargs_func(argc, (void*)*argv);
    return result;
}
```

