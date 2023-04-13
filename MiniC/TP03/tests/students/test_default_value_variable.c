#include "printlib.h"

int main()
{
  int INT;
  float FLOAT;
  bool BOOL;

  println_int(INT);
  println_float(FLOAT);
  println_bool(BOOL);
  return 0;
}

// EXPECTED
// 0
// 0.00
// 0
