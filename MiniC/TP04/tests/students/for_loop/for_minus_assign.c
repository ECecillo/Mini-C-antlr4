#include "printlib.h"

int main()
{
  int i;
  for (i = 5; i > 0; i = i - 1)
  {
    println_int(i);
  }

  return 0;
}

// EXPECTED
// 5
// 4
// 3
// 2
// 1