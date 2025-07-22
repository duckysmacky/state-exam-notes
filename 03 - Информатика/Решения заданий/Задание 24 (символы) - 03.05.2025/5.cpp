#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int main()
{
    string text;
    ifstream file("5.txt");
    getline(file, text);

    // text = "abc^de$f#g^hi$jkl#m^no$pqrs^$t#u^vw$xyz#a$bcd^efgh";

    vector<size_t> substrs;
    int i = 0, j = 0;
    while (i < text.length())
    {
        string substr = string(text.begin() + i, text.begin() + j);

        int cnt_up = count(substr.begin(), substr.end(), '^');
        int cnt_dollar = count(substr.begin(), substr.end(), '$');
        int cnt_hash = count(substr.begin(), substr.end(), '#');

        cout << i << ' ' << j << endl;

        if (cnt_up + cnt_dollar == 76 && cnt_hash <= 3)
        {
            substrs.push_back(substr.length());
        }

        if (j >= text.length())
        {
            i++;
            j = i;
        }

        j++;
    }

    size_t best = *max_element(substrs.begin(), substrs.end());
    cout << best << endl;

    return 0;
}