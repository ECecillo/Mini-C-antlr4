#include "printlib.h"

int main()
{
  int x, y, z;
  x = 15;
  y = 3;

  if (x > 10)
  {
    while (x > 10)
    {
      x = x - 1;
      z = z + 1;
    }
    y = y + 1;
  }

  println_int(x);
  println_int(y);
  println_int(z);
  return 0;
}

// EXPECTED
// 10
// 4
// 5
