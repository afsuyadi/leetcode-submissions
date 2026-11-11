function removeDuplicates(s: string): string {
    const uniqueArray: string[] = [];
    for (const ss of s) {
        if (uniqueArray.length !== 0 && uniqueArray[uniqueArray.length - 1] === ss) {
            uniqueArray.pop()
        } else {
            uniqueArray.push(ss)
        }
    }
    return uniqueArray.join('')
};