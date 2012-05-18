Save Humanity(30points)
=======================

Oh!! Mankind is in trouble again.This time its a deadly disease spreading at a rate never seen before. Efficient detectors for the virus responsible is the need of the hour. You are the lead at Central Hospital and need to find a fast and reliable way to detect the 'foot-prints' of the virus DNA in that of patient.

The DNA of the patient as well as of the virus consists of lower case letters. Since the data collected is raw there may be some errors. You will need to find all substrings in the patient DNA that exactly matches the virus DNA with the exception of at most one mismatch.

For example tolerating at most one mismatch, "aa" and "aa" are matching, "ab" and "aa" are matching, while "ab" and "ba" are not.

**Input:**

The first line contains the number of test cases T. T cases follow. Each case contains two lines containing strings P(Patient DNA) and V(Virus DNA) . Each case is followed by a blank line.

**Output:**

Output T lines, one corresponding to each case. For each case, output a space delimited list of starting indices (0 indexed) of substrings of P which are matching with V according to the condition mentioned above . The indices has to be in increasing order.

**Constraints:**

1 <= T <= 10

P and V contain at most 100000 characters each.

All characters in P and V are lowercase letters.

**Sample Input:**

	3
	abbab
	ba
	
	 
	
	hello
	
	world
	
	 
	
	banana
	
	nan


**Sample Output:**

	1 2
	
	 
	
	0 2

**Explanation:**

For the first case, the substrings of P starting at indices 1 and 2 are "bb" and "ba" and they are matching with the string V which is "ba".
For the second case, there are no matching substrings so the output is a blank line.