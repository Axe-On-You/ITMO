#include <iostream>

using namespace std;

long long q, w, e, r, t, y, u, i, o, p, a[10005], s, d, f;

int main() {
  if (cin >> q >> w) {
    e = 0;
    while (e < 10005) {
      a[e] = 0;
      e = e + 1;
    }

    r = 0;
    while (r < q) {
      cin >> t;
      a[t] = a[t] + 1;
      r = r + 1;
    }

    y = 0;
    u = 10000;
    i = 1;

    while (u > 0) {
      o = a[u];
      while (o > 0) {
        if (i == w) {
          i = 1;
          p = 0;
        } else {
          y = y + u;
          i = i + 1;
          s = 1;
        }
        o = o - 1;
        if (s == 1) {
          d = 0;
        }
      }
      u = u - 1;
    }

    cout << y << "\n";
  }
  return 0;
}