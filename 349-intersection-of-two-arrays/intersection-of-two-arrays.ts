function intersection(nums1: number[], nums2: number[]): number[] {
    const interArray: number[] = []
    nums1.sort((a,b) => a-b);
    nums2.sort((a,b) => a-b);
    for (const num1 of nums1) {
        for (const num2 of nums2) {
            if (num1 === num2 && !interArray.includes(num1)) {
                interArray.push(num1)
            }
        }
    }
    return interArray
};
