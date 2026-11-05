function intersect(nums1: number[], nums2: number[]): number[] {
    nums1.sort((a,b) => a-b);
    nums2.sort((a,b) => a-b);
    const mapNums1 = new Map<number, number>([]);
    const mapNums2 = new Map<number, number>([]);
    const result:number[] = [];
    // console.log('Nums1=', nums1)
    // console.log('Nums2=', nums2)
    for (let i = 0; i < nums1.length; i++) {
        for (let j = 0; j < nums2.length; j++) {
            // console.log('!mapNums1.get(i)', !mapNums1.has(i))
            // console.log('!mapNums2.get(j)', !mapNums2.has(j))
            if (nums1[i] === nums2[j] && !mapNums1.has(i) && !mapNums2.has(j)) {
                result.push(nums1[i]);
                mapNums1.set(i, nums1[i])
                mapNums2.set(j, nums2[j])
            }
        }
    }
    return result
};
