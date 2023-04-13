#include "printlib.h"

int main()
{
  int x, y;
  x = 15;
  y = 3;

  while(x > 10)
  {
    y = y + 1;
    x = x - 1;
  }

  println_int(x);
  println_int(y);
  return 0;
}

// EXPECTED
// 10
// 8
