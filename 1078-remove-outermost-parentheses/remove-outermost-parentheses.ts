function removeOuterParentheses(s: string): string {
    let count: number = 0;
    let result: string = "";
    for (const val of s) {
        if (val === '(') {
            if (count > 0) {
                result = result + val;
            }
            count = count + 1;
        } else if (val === ')') {
            count = count - 1;
            if (count > 0) {
                result = result + val;
            }
        }
    }
    return result
};
