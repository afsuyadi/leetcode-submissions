function majorityElement(nums: number[]): number {
    const dictelement = new Map<number, number>([])
    for (const num of nums) {
        const dictvalue = dictelement.get(num) ?? 0
        if (dictvalue) {
            dictelement.set(num, dictvalue + 1)
        } else {
            dictelement.set(num, 1)
        }
    }
    let majorityNum = -1;
    let maxCount = 0;
    for (const [num, count] of dictelement) {
        if (count > maxCount) {
            maxCount = count;
            majorityNum = num;
        }
    }
    return majorityNum
};