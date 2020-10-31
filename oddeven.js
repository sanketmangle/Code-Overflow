const oddeven = (number) => {
    if(typeof number !== "number") {
        console.log("Error: NaN")
    } else {
        if(number % 2 === 0) {
            console.log("Even!")
        } else if(number % 2 !== 0) {
            console.log("Odd!")
        }
    }
}