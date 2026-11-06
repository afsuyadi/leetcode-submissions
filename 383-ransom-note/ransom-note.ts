
function canConstruct(ransomNote: string, magazine: string): boolean {
    if (ransomNote.length > magazine.length) return false;
    const ransomMap = new Map<string, number>([]);
    const magaMap = new Map<string, number>([]);

    for (const ra of ransomNote) {
        const raVal = ransomMap.get(ra)!; // {ra: raVal}
        if (raVal) {
            ransomMap.set(ra, raVal + 1)
        } else {
            ransomMap.set(ra, 1)
        }
    }

    for (const ma of magazine) {
        const maVal = magaMap.get(ma)!; // {ra: raVal}
        if (maVal) {
            magaMap.set(ma, maVal + 1)
        } else {
            magaMap.set(ma, 1)
        }
    }

    for (const [char, count] of ransomMap) {
        const magCount = magaMap.get(char) ?? 0;
        if (count > magCount) return false;
    }
    return true
};
