#include "printlib.h"

int main()
{
  int i, compteur;
  for (; ;)
  {
    if (compteur == 100)
    {
      println_int(10 / 0);
    }
    compteur = compteur + 1;
  }

  return 0;
}

// EXECCODE 1
// SKIP TEST EXPECTED
// EXPECTED
// Division by 0
