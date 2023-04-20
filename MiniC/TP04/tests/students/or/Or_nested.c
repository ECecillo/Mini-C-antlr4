#include "printlib.h"

int main()
{
  bool isFalse, isTrue;
  isFalse = false;
  isTrue = true;

  if ((isFalse || isTrue) || (isFalse || (isTrue || isFalse)))
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
// 42
