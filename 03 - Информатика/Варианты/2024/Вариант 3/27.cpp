#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int sum(const vector<int> &vec)
{
    int sum = 0;
    for (auto val : vec)
        sum += val;
    return sum;
}

bool sumSort(const vector<int> &a, const vector<int> &b)
{
    return (sum(a) > sum(b));
}

void printVector(const vector<int> &vec)
{
    for (auto val : vec)
        cout << val << " ";
    cout << endl;
}

int main()
{
    ifstream file("27/27-B.txt");

    int N = 0;
    vector<int> nums;

    string line;
    while (getline(file, line))
    {
        if (N == 0)
            N = stoi(line);
        else
            nums.push_back(stoi(line));
    }

    vector<vector<int>> slices;
    int i = 0, j = 0;
    while (i < N)
    {
        vector<int> slice(nums.begin() + j, nums.begin() + i + 1);
        if (sum(slice) % 107 == 0)
        {
            slices.push_back(slice);
        }

        j++;
        if (j > i)
        {
            j = 0;
            i++;
        }
    }

    sort(slices.begin(), slices.end(), sumSort);
    for (auto slc : slices)
    {
        cout << sum(slc) << " - " << slc.size() << endl;
    }
}