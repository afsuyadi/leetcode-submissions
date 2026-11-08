
function isValid(s: string): boolean {
    let currentStack: string[] = [];
    let openPar: string[] = ["(", "[", "{"];
    const couplePar = new Map<string, string>([
        ["(", ")"],
        ["{", "}"],
        ["[", "]"],
    ])
    for (const par of s) {
        if (openPar.includes(par)) { // par is open
            currentStack.push(par)
        } else {
            const top = currentStack.pop();
            if (top === undefined || couplePar.get(top) !== par) {
                return false
            }
        }
    }
    return currentStack.length === 0
};
