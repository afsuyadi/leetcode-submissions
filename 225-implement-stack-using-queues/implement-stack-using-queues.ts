
class MyStack {
    private array: number[];
    constructor() {
        this.array = [];
    }

    push(x: number): void {
        this.array.push(x)
        let n = this.array.length;
        while (n>1) {
            const backest = this.array.shift()!;
            this.array.push(backest);
            n--;
        }
    }

    pop(): number {
        return this.array.shift()!
    }

    top(): number {
        return this.array[0]
    }

    empty(): boolean {
        return this.array.length === 0
    }
}