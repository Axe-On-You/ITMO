#include <cctype>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

struct Object {
  char type;  // A, a, B, b ...
  int id;     // Нмоер во входной строке
};

int main() {
  string s;
  if (!(cin >> s)) {
    return 0;
  }

  int n = s.length() / 2;  // Кол-во видов
  stack<Object> st;
  vector<int> result(n + 1);

  int animals = 0;
  int traps = 0;
  vector<int> current_id(s.length());
  for (int i = 0; i < static_cast<int>(s.length()); i++) {
    if (islower(s[i]) != 0) {
      current_id[i] = ++animals;
    } else {
      current_id[i] = ++traps;
    }
  }
  for (int i = 0; i < static_cast<int>(s.length()); i++) {
    if (!st.empty()) {
      char top_char = st.top().type;
      char current_char = s[i];

      if (tolower(top_char) == tolower(current_char) && top_char != current_char) {
        int top_index = current_id[st.top().id];
        int curr_index = current_id[i];
        if (islower(current_char) != 0) {  // curr - животное, top - ловушка
          result[top_index] = curr_index;
        } else {  // наоборот
          result[curr_index] = top_index;
        }

        st.pop();
        continue;
      }
    }
    st.push({s[i], i});
  }

  if (st.empty()) {
    cout << "Possible" << endl;
    for (int i = 1; i <= n; i++) {
      cout << result[i] << (i == n ? "" : " ");
    }
    cout << endl;
  } else {
    cout << "Impossible" << endl;
  }

  return 0;
}