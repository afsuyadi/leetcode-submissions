function romanToInt(s: string): number {
    const romandict = new Map<string, number>([
        ["I", 1],
        ["V", 5],
        ["X", 10],
        ["L", 50],
        ["C", 100],
        ["D", 500],
        ["M", 1000],
    ])
    let idx = 0
    let res = 0
    while (idx < s.length) {
        const current = romandict.get(s[idx])!
        const next = romandict.get(s[idx + 1])
        if (current < next) {
            res = res - current
        } else {
            res = res + current
        }
        idx ++;

    }
    
    return res
};