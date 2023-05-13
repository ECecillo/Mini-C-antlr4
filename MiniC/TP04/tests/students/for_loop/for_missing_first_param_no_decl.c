#include "printlib.h"

int main()
{
  int compteur;
  for (; i < 5; i++)
  {
    if (compteur == 1000)
    {
      println_int(1 / 0);
    }
    compteur = compteur + 1;
  }
  return 0;
}
// EXPECTED
// EXITCODE 2
// In function main: Line 6 col 9: Undefined variable i
