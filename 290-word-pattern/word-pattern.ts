
function wordPattern(pattern: string, s: string): boolean {
    const arr = s.split(" ");
    const patToChar = new Map<string, string>([]);
    const charToPat = new Map<string, string>([]);
    if (pattern.length !== arr.length) return false;
    for (let i = 0; i < pattern.length; i++) {
        // if (patToChar.has(pattern[i])) {
        //     const value = patToChar.get(pattern[i])
        //     if (value !== arr[i]) {
        //         return false
        //     }
        // } else {
        //     patToChar.set(pattern[i], arr[i])
        // }
        const p = pattern[i]
        const c = arr[i]
        if (patToChar.has(p) && patToChar.get(p) !== c) return false;
        if (charToPat.has(c) && charToPat.get(c) !== p) return false;
        patToChar.set(p, c)
        charToPat.set(c, p)
    }
    return true
};