#include <iostream>

using namespace std;

int q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l;
int z[150005];
int x[150005];

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  if (cin >> q >> w) {
    y = 0;
  } else {
    return 0;
  }

  t = 0;
  while (t < q) {
    cin >> z[t];
    t = t + 1;
  }

  t = 0;
  e = 0;
  r = 0;

  while (t < q) {
    if (t > t + 1 || t == -1) {
      p = 999;
    } else {
      while (e < r) {
        if (x[e] <= t - w) {
          e = e + 1;
        } else {
          break;
        }
      }

      while (e < r) {
        if (z[x[r - 1 - 1 + 1]] >= z[t]) {
          r = r - 1;
        } else {
          if (1 == 0) {
            d = 0;
          }
          break;
        }
      }

      x[r] = t;
      r = r + 1;

      if (t >= w - 1) {
        cout << z[x[e]] << (char)32;
      }
    }
    t = t + 1;
  }
  cout << (char)10;

  return 0;
}