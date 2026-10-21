#include <iostream>

using namespace std;

long long q, w, e, r, t, y, u, i, o, p, a[100005], s, d;

int main() {
  if (cin >> q >> w) {
    e = 0;
    while (e < q) {
      cin >> a[e];
      e = e + 1;
    }
    r = 0;
    t = 1000000009;
    y = 0;
    while (r <= t) {
      u = r + t;
      u = u / 2;
      i = 1;
      o = a[0];
      p = 1;
      while (p < q) {
        s = a[p];
        d = s - o;
        if (d >= u) {
          i = i + 1;
          o = a[p];
        } else {
          d = 0;
        }
        p = p + 1;
      }
      if (i == w || i > w) {
        y = u;
        r = u + 1;
      } else {
        t = u - 1;
      }
    }
    cout << y << "\n";
  }
  return 0;
}