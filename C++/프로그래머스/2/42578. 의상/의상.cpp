#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 0, acc = 1;
    unordered_map<string, vector<string>> closet;
    vector<string> clothes_type;
    for (const vector<string>& c : clothes) {
        closet[c[1]].push_back(c[0]);
        clothes_type.push_back(c[1]);
    }
    for (const auto& [key, value] : closet) {
        acc *= value.size() + 1;
    }
    answer = acc - 1;
    return answer;
}