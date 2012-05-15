Matrix (25 pts)
===============

https://www.interviewstreet.com/challenges/dashboard/#problem/4f904e704e404

Machines have once again attacked the kingdom of Xions.  The kingdom of Xions has N cities and N-1 bidirectional roads. The road network is such that there is a unique path between any pair of cities.

Morpheus has the news that K Machines are planning to destroy the whole kingdom. These Machines are initially living in K different cities of the kingdom and anytime from now they can plan and launch an attack. So he has asked Neo to destroy some of the roads to disrupt the connection among Machines i.e after destroying those roads there should not be any path between any two Machines.

Since the attack can be at any time from now, Neo has to do this task as fast as possible. Each road in the kingdom takes certain time to get destroyed and they can be destroyed only one at a time. 

You need to write a program that tells Neo the minimum amount of time he will require to disrupt the connection among machines.

Sample Input**

First line of the input contains two, space-separated integers, N and K. Cities are numbered 0 to N-1.
Then follow N-1 lines, each containing three, space-separated integers, x y z, which means there is a bidirectional road connecting city x and city y, and to destroy this road it takes z units of time.
Then follow K lines each containing an integer. Ith integer is the id of city in which ith Machine is currently located.

**Output Format**

Print in a single line the minimum time required to disrupt the connection among Machines.

**Sample Input**

    5 3
    2 1 8
    1 0 5
    2 4 5
    1 3 4
    2
    4
    0

**Sample Output**

    10

**Explanation**

Neo can destroy the road connecting city 2 and city 4 of weight 5 , and the road connecting city 0 and city 1 of weight 5. As only one road can be destroyed at a time, the total minimum time taken is 10 units of time. After destroying these roads none of the Machines can reach other Machine via any path.

**Constraints**

2 <= N <= 100,000
2 <= K <= N
1 <= time to destroy a road <= 1000,000