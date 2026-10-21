function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    const nextGreater = new Map<number, number>(); // map
    const stack: number[] = [];

    for (const n of nums2) {
        while (stack.length > 0 && stack[stack.length - 1] < n) { // make sure stack is not empty and the most top stack value is smaller than n
            const top = stack.pop()!;
            nextGreater.set(top, n);
            // console.log('nextGreater=', nextGreater)
        }
        stack.push(n);
    }
    return nums1.map(x => nextGreater.get(x) ?? -1);
};