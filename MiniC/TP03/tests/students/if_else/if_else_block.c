#include "printlib.h"

int main()
{
  int x, y;
  x = 12;
  y = 3;

  if (y > 10)
  {
    x = 1;
    y = 2;
  }
  else
  {
    x = 3;
    y = 4;
  }

  println_int(x);
  println_int(y);
  return 0;
}

// EXPECTED
// 3
// 4
