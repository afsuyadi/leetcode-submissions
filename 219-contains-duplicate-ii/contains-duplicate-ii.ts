function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const collect = new Map<number, number>([]);
    for (let i = 0; i < nums.length; i++) {
        if (collect.has(nums[i])) {
            if (Math.abs(i - collect.get(nums[i])!) <= k) {
                return true
            } else {
                collect.set(nums[i], i)
            }
        } else {
            collect.set(nums[i], i)
        }
        // for (let j = i + 1; j < nums.length; j ++) {
        //     if (nums[i] === nums[j] && Math.abs(i-j) <= k) {
        //         return true
        //     }
        // }

    }
    return false
};