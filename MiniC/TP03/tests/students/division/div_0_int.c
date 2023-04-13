#include "printlib.h"

int main()
{
  int x;
  x = 0 / 10;

  println_int(x);
  return 0;
}

// EXPECTED
// 0
