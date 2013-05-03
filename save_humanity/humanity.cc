#include <iostream>
#include <string.h>

using namespace std;

void findMatches(char* patient, char* virus) {
	int patLen = strlen(patient);
	int virLen = strlen(virus);

	if (patLen < virLen) {
		return;
	}

	bool hadError = false, allMatch = true;
	int i, j;

	// try all possible starts for the virus
	for (i = 0; i < patLen - virLen + 1; ++i) {
		hadError = false;
		allMatch = true;

		// try to match virus, allow one error
		for (j = 0; j < virLen; ++j) {
			if (patient[i + j] != virus[j]) {
				if (hadError) {
					allMatch = false;
					break;
				}
				else {
					hadError = true;
				}
			}
		}

		if (allMatch) {
			cout << i << " ";
		}
	}

	cout << endl;
}

int main() {
    int i, n;
    char patient[1000001], virus[100001];

    // read number of patients
    cin >> n;

    for (i = 0; i < n; ++i) {
    	// read strings
        cin >> patient;
        cin >> virus;

        // find matches
        findMatches(patient, virus);
    }

    return 0;
}
