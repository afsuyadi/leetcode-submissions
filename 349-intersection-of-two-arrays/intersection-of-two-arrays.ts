//  11 ms (4/11)
function intersection(nums1: number[], nums2: number[]): number[] {
    // const interArray: number[] = []
    // nums1.sort((a,b) => a-b);
    // nums2.sort((a,b) => a-b);
    // for (const num1 of nums1) {
    //     for (const num2 of nums2) {
    //         if (num1 === num2 && !interArray.includes(num1)) {
    //             interArray.push(num1)
    //         }
    //     }
    // }
    // return interArray
    const set1 = new Set(nums1)
    const set2 = new Set(nums2)
    const result:number[] = [];
    // console.log('Set1=', set1)
    // console.log('Set2=', set2)
    for (const num1 of set1) {
        if (set2.has(num1)) {
            result.push(num1);
        }
    }
    return result
};