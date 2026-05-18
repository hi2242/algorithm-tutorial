#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(const string& a, const string& b);

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> v;
    for (int i : numbers) {
        v.push_back(to_string(i));
    }
    sort(v.begin(), v.end(), cmp);
    
    for (string s : v) {
        answer += s;
    }
    
    if (answer[0] == '0') {
        answer = "0";
    }
    return answer;
}

bool cmp(const string& a, const string& b) {
    return a + b > b + a;
}