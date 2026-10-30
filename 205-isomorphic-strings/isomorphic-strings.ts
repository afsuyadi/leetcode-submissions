function isIsomorphic(s: string, t: string): boolean {
    let mapST = new Map<string, string>();
    let mapTS = new Map<string, string>();
    if (s.length !== t.length) {
        return false
    }
    // ex: mapST = {'e': 'a', 'g':'d'}
    //  ex: mapTS = {'a': 'e', 'd':'g'}
    for (let i = 0; i < s.length; i++) {
        const sc = s[i] // ex: 'e'
        const tc = t[i] // ex: 'a'
        const checkSInsideT = mapST.get(sc)
        const checkTInsideS = mapTS.get(tc)
        if (checkSInsideT || checkTInsideS) {
            if (checkTInsideS === sc && checkSInsideT === tc) {
                continue
            } else {
                return false
            }
        } else {
            mapST.set(sc, tc)
            mapTS.set(tc, sc)
        }
    }
    return true
};