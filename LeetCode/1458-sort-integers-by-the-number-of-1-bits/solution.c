
#include <stdio.h>
#include <stdlib.h>

int countSetBits(int num) {
    int count = 0;
    while (num) {
        count += num & 1;
        num >>= 1;
    }
    return count;
}

int compare(const void* a, const void* b) {
    int intA = *(int*)a;
    int intB = *(int*)b;

    int countA = countSetBits(intA);
    int countB = countSetBits(intB);

    if (countA == countB) {
        return (intA < intB) ? -1 : (intA > intB) ? 1 : 0;
    } else {
        return (countA < countB) ? -1 : 1;
    }
}

int* sortByBits(int* arr, int arrSize, int* returnSize) {
    qsort(arr, arrSize, sizeof(int), compare);
    *returnSize = arrSize;
    return arr;
}


