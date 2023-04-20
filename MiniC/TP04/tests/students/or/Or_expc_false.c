#include "printlib.h"

int main()
{
  bool isFalse, isTrue;
  isFalse = false;
  isTrue = true;

  if (isFalse || isFalse)
  {
    println_int(42);
  }
  else
  {
    println_int(30);
  }
  return 0;
}

// EXPECTED
// 30
