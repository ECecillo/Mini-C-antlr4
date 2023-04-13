#include "printlib.h"

int main()
{
  int x, y, z;
  x = 15;
  y = 5;

  while (x > 10)
  {
    y = y + 2;
    x = x - 1;
    if(x == 12) { println_string("coucou"); }
    while (y < 13) {
      z = z + 1;
      y = y + 1;
    }
  }

  println_int(x);
  println_int(y);
  println_int(z);
  return 0;
}

// EXPECTED
// coucou
// 10
// 21
// 6
