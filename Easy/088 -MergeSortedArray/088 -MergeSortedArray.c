void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {

    int i = 0, j = 0, k = 0;

    int merged[m + n];

    while (i < m && j < n) {

        if (nums1[i] <= nums2[j]) {
            merged[k++] = nums1[i++];
        }
        else {
            merged[k++] = nums2[j++];
        }
    }

    if (i < m) {
        while (i < m) {
            merged[k++] = nums1[i++];
        }
    }
    else {
        while (j < n) {
            merged[k++] = nums2[j++];
        }
    }
    for (int i = 0; i < m + n; i++) {
    nums1[i] = merged[i];
}
}