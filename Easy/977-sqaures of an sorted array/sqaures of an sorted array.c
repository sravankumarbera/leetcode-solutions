/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 //leet code problem 977 (squares of a sorted array)solution 
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int i = 0, j = numsSize - 1, k = numsSize - 1;
    int* squares = malloc(numsSize * sizeof(int));

    while (i <= j) {
        if (nums[i] * nums[i] > nums[j] * nums[j]) {
            squares[k] = nums[i] * nums[i];
            i++;
        } else {
            squares[k] = nums[j] * nums[j];
            j--;
        }

        k--;
    }

    *returnSize = numsSize;
    return squares;
}