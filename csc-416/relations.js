class Relation {
    constructor(setA=[], setB=null){
        this.orderedPairs = [];
        this.setA = setA;
        this.setB = setB;
        this.elements = new Set(setA.concat(setB ?? []));
    }
    createRelation(condition){
        this.setA.forEach((a) => {
            if(this.setB !== null && Array.isArray(this.setB)){
                this.setB.forEach((b) => {
                    if(condition([a,b])){
                        this.orderedPairs.push([a,b]);
                    }
                })
            }
            this.setA.forEach((a1) => {
                if(condition([a,a1])){
                    this.orderedPairs.push([a,a1]);
                }
            })
        })
    }
    isReflexive() {
        let count = 0;
        this.orderedPairs.forEach((pair) => {
            const [a,b] = pair;
            if(a === b ) count+=1;
        })
        return count === this.elements.size;
    }
    isSymmetric() {
        let count = 0;
        this.orderedPairs.forEach((pair,index) => {
            const [a1,b1] = pair;
            this.orderedPairs.slice(index + 1).forEach((pair2) => {
                const [a2,b2] = pair2;
                if (b1 === a2 && b2 === a1){
                    count+=1;
                }
            })
        })
        return count > 0;
    }
    isAntiSymmetric() {

    }
    isTransitive(){

    }
    printOrderedPairs() {

    }
}