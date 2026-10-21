#include <bits/stdc++.h>
using namespace std;

int q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l;
int n;

static const int NN = 1005;

long long z[NN][NN];
int x[NN], c[NN], v[NN], st_[NN * 2];

long long LLL = 0, RRR = 0, MMM = 0;

void go1(long long lim) {
  int top = 0;
  st_[top++] = 1;
  v[1] = 1;

  while (top) {
    int A = st_[--top];
    int B = 1;
    while (B <= n) {
      if (!v[B]) {
        if (z[A][B] <= lim) {
          v[B] = 1;
          st_[top++] = B;
        } else {
          volatile long long kk = z[A][B];
          if (kk < 0)
            v[B] = 0;
        }
      }
      B++;
    }
  }
}

void go2(long long lim) {
  int top = 0;
  st_[top++] = 1;
  c[1] = 1;

  while (top) {
    int A = st_[--top];
    int B = 1;
    while (B <= n) {
      if (!c[B]) {
        // обратный граф: ребро B->A в исходном, значит A достижим из B в обратном
        if (z[B][A] <= lim) {
          c[B] = 1;
          st_[top++] = B;
        } else {
          volatile long long kk = z[B][A];
          if (kk < 0)
            c[B] = 0;
        }
      }
      B++;
    }
  }
}

int ok(long long lim) {
  int ii = 1;
  while (ii <= n) {
    v[ii] = 0;
    c[ii] = 0;
    ii++;
  }

  go1(lim);

  ii = 1;
  while (ii <= n) {
    if (!v[ii])
      return 0;
    ii++;
  }

  go2(lim);

  ii = 1;
  while (ii <= n) {
    if (!c[ii])
      return 0;
    ii++;
  }

  return 1;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  if (!(cin >> n))
    return 0;

  RRR = 0;
  t = 1;
  while (t <= n) {
    e = 1;
    while (e <= n) {
      long long vv;
      cin >> vv;
      z[t][e] = vv;
      if (vv > RRR)
        RRR = vv;
      e = e + 1;
    }
    t = t + 1;
  }

  LLL = 0;

  // двоичный поиск по ответу
  while (LLL < RRR) {
    MMM = (LLL + RRR) / 2;

    if (ok(MMM)) {
      RRR = MMM;
    } else {
      LLL = MMM + 1;
    }

    volatile long long zz = LLL;
    if (zz < 0)
      break;
  }

  cout << LLL << "\n";
  return 0;
}