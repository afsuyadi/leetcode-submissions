
class MyQueue {
    private inArray: number[];
    private outArray: number[];
    constructor() {
        this.inArray = [];
        this.outArray = [];
    }

    push(x: number): void {
        this.inArray.push(x)
    }

    pop(): number {
        // remember, FIFO. Uses stack Operators.
        if (this.outArray.length === 0) {
            while (this.inArray.length !== 0) {
                const popIn = this.inArray.pop()!;
                this.outArray.push(popIn)
            }            
        }
        return this.outArray.pop()!;        
    }

    peek(): number {
        if (this.outArray.length === 0) { 
            while (this.inArray.length !== 0) {
                const popIn = this.inArray.pop()!;
                this.outArray.push(popIn)
            }
        }
        
        return this.outArray[this.outArray.length - 1];
    }

    empty(): boolean {
        return this.outArray.length === 0 && this.inArray.length === 0;
    }
}