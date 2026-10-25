function twoSum(nums: number[], target: number): number[] {
    const map = new Map<number, number>();
    for (const [i, val] of nums.entries()) {
        const diff = target - val
        if (map.has(diff)) {
            console.log(map)
            return [map.get(diff)!, i]
        }
        map.set(val, i);
        
    }
};
