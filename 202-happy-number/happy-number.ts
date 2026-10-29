function isHappy(n: number): boolean {
    let nstr = String(n);
    let seenNumbers: number[] = [];
    while (true) {
        const total = sumOfString(nstr);
        if (total === 1) {
            return true
        } 
        if (seenNumbers.includes(total)){
            return false
        } else {
            nstr = String(total)
            seenNumbers.push(total)
        }
    }
    return false
};

function sumOfString(nstr: string): number{
    let total = 0;
    for (const n of nstr) {
        const nnum = Number(n) * Number(n)
        total = total + nnum
    }
    return total
}