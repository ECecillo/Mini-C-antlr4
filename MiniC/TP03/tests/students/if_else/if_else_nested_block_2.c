#include "printlib.h"

int main()
{
  int x, y, res;
  x = 12;
  y = 3;

  if (x > 10)
  {
    res = x + y;
    if (res < x)
    {
      x = 3;
      y = 4;
    }
    else
    { // Go here
      x = 5;
      y = 6;
    }
  }

  println_int(x);
  println_int(y);
  return 0;
}

// EXPECTED
// 5
// 6
