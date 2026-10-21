#include <cctype>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string s;
  cin >> s;
  vector<int> result;
  size_t i = 0;

  if (s.length() % 2 != 0) {
    cout << "Impossible";
    return 0;
  }

  while (s.length() > 0) {
    if (i >= s.length() - 1) {
      cout << "Impossible";
      return 0;
    }
    if (tolower(s[i]) == tolower(s[1 + i])) {
      if (isupper(s[i])) {
        result.push_back(i);
      } else {
        result.push_back(i + 1);
      }
      s.erase(i, 2);
      i = 0;
    } else if (i < s.length() - 1) {
      i++;
    }
  }
  if (s.length() == 0) {
    cout << "Possible\n";
    for (size_t i = 0; i < result.size(); i++) {
      cout << result[i] << " ";
    }
  } else {
    cout << "Impossible";
  }

  return 0;
}
