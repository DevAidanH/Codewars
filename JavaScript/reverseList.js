function reverseSeq(n){
    output = []
    for(let i = n; i > 0; i--){
        output.push(i)
    }
    return output
}

console.log(reverseSeq(5))