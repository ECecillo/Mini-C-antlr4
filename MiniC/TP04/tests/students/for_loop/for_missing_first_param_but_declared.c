#include "printlib.h"

int main()
{
  int i, compteur;
  compteur = 0;
  for (; i < 5; i++)
  {
    println_int(i);
  }
  return 0;
}
// EXPECTED
// 0
// 1
// 2
// 3
// 4
