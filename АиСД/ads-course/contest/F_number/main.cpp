#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string a[105], z, x, c, v, b;
long long q, w, e, r, t;

int main() {
  freopen("number.in", "r", stdin);
  freopen("number.out", "w", stdout);

  q = 0;
  while (cin >> z) {
    a[q] = z;
    q = q + 1;
  }

  w = 0;
  while (w < q) {
    e = 0;
    t = q - 1;
    while (e < t) {
      x = a[e];
      c = a[e + 1];
      v = x + c;
      b = c + x;

      if (v < b) {
        a[e] = c;
        a[e + 1] = x;
      } else {
        r = 0;
      }

      if (r == 0) {
        e = e + 1;
      }
    }
    w = w + 1;
  }

  w = 0;
  while (w < q) {
    cout << a[w];
    w = w + 1;
    if (w == q) {
      cout << "";
    }
  }

  cout << "\n";
  return 0;
}