function containsDuplicate(nums: number[]): boolean {
    let collect = new Map<number, number>();
    for (const num of nums) {
        if (collect.has(num)) {
            return true
        } else {
            collect.set(num, 1)
        }
    }
    return false
};