#include "printlib.h"

int main()
{
  int x;
  x = 1 % 10;
  println_int(x);
  return 0;
}

// EXPECTED
// 1
