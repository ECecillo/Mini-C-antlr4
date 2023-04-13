#include "printlib.h"

int main()
{
  int x, y;
  x = 12;
  y = 3;

  if (x > 10)
  {
    x = 1;
    y = 2;
  }

  println_int(x);
  println_int(y);
  return 0;
}

// EXPECTED
// 1
// 2
