#include <iostream>
#include <string.h>

using namespace std;

int similaritySum(char* str) {
	int i, j;

	int length = strlen(str);
	int simSum = length;

	// for all suffixes
	for (i = 1; i < length; ++i) {
		// count length of common prefix
		for (j = 0; j < length - i; ++j) {
			if (str[j] == str[i + j]) {
				++simSum;
			}
			else {
				break;
			}
		}
	}

	return simSum;
}

int main() {
    int i, n;
    char str[1000001];

    // read number of strings
    cin >> n;

    for (i = 0; i < n; ++i) {
    	// read string
        cin >> str;

        // compute and print similarity sum
        cout << similaritySum(str) << endl;
    }

    return 0;
}
