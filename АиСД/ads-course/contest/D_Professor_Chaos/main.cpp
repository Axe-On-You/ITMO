#include <iostream>

using namespace std;

long long q, w, e, r, t, y;

int main() {
  if (cin >> q >> w >> e >> r >> t) {
    y = -100;
    long long u = 0;
    while (u < t) {
      long long z = q * w;
      z = z - e;
      if (z < 0) {
        z = 0;
      }
      if (z > r) {
        z = r;
      }
      if (z == y) {
        q = z;
        u = t;
      } else {
        y = z;
        q = z;
        u = u + 1;
      }
      if (q == 0) {
        u = t;
      }
    }
    cout << q << "\n";
  }
  return 0;
}