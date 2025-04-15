function reverseSeq(n){
    o = []
    for(let i = n; i > 0; i--){
        o.push(i)
    }
    return o
}

console.log(reverseSeq(5))