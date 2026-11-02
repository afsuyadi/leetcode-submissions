
function isAnagram(s: string, t: string): boolean {
    const sMap = new Map<string, number>([])
    if (s.length !== t.length) return false;
    for (const letter of s) {
        sMap.set(letter, (sMap.get(letter) ?? 0) + 1)
    }
    const tMap = new Map<string, number>([])
    for (const letter of t) {
        tMap.set(letter, (tMap.get(letter) ?? 0) + 1)
    }
    if (sMap.size !== tMap.size) return false;
    for (const [key, val] of sMap) {
        if (!tMap.get(key) || tMap.get(key) !== val) return false;
    }
    for (const [key, val] of tMap) {
        if (!sMap.get(key) || sMap.get(key) !== val) return false;
    }
    return true
};