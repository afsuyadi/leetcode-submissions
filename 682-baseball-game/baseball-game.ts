function calPoints(operations: string[]): number {
    const stack: number[] = [];
    for (const op of operations) {
        const isNumber = Number(op)
        if (typeof isNumber === "number" && Number.isInteger(isNumber)) {
            stack.push(isNumber)
        } else if (op === '+') {
            const topFirst = stack[stack.length - 1]
            const topSecond = stack[stack.length - 2]
            const newTop = topFirst + topSecond
            stack.push(newTop)
        } else if (op === 'D') {
            const topFirst = stack[stack.length - 1]
            const newTop = topFirst * 2
            stack.push(newTop)
        } else if (op === 'C') {
            stack.pop()
        }
    }
    const sum = stack.reduce((acc, val) => acc + val, 0)
    return sum
};