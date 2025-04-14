//Function to evaluate if you can make it to a fuel station
function zeroFuel(distanceToPump, mpg, fuelleft){
    if((fuelleft*mpg)>=distanceToPump){
        return true
    }
    else{
        return false
    }
}

//Tests
console.log(zeroFuel(50, 25, 2))
console.log(zeroFuel(100, 50, 1))