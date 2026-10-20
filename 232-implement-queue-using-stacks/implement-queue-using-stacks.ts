class MyQueue {
    private inStack: number[];
    private outStack: number[];

    constructor() {
        this.inStack = [];
        this.outStack = [];
    }

    push(x: number): void {
        this.inStack.push(x)
    }

    pop(): number {
        if (this.outStack.length === 0) {
            while (this.inStack.length > 0) {
                const popped = this.inStack.pop()!
                this.outStack.push(popped)
            }
        }
        return this.outStack.pop()!
    }

    peek(): number {
        if (this.outStack.length === 0) {
            while (this.inStack.length > 0) {
                const popped = this.inStack.pop()!
                this.outStack.push(popped)
            }
    }   return this.outStack[this.outStack.length - 1]
}

    empty(): boolean {
        if (this.inStack.length === 0 && this.outStack.length === 0) {
            return true
        }
        return false
    }
}