#include "printlib.h"

int main()
{
  int a, b;
  a = 42;
  b = 18;

  println_int(a / b);

  return 0;
}

// EXPECTED
// 2
