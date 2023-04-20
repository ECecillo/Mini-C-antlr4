#include "printlib.h"

int main()
{

  int x;
  x = 10;
  while (x > 0)
  {
    println_int(x);
    if (x == 5)
    {
      println_int(x);
    }
    x = x - 1;
  }

  return 0;
}

// EXPECTED
// 10
// 9
// 8
// 7
// 6
// 5
// 5
// 4
// 3
// 2
// 1
