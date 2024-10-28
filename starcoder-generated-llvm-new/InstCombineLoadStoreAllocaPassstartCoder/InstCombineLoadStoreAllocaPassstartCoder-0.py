
```c
#include <string.h>

int main() {
  const char* data = "hello, world!";
  char* buffer = (char*)malloc(strlen(data) + 1);
  
  if (buffer) {
    memcpy(buffer, data, strlen(data) + 1);
    free(buffer);
  }
  
  int result = 0;
  
  if (buffer[0] == data[0] && buffer[1] == data[1]) {
    result = 1;
  } else {
    result = 0;
  }
  
  return result;
}
```

