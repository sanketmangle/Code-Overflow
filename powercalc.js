let powercalc = (base, power) => {
    if(typeof base !== "number" || typeof power !== "number") {
        console.log("Error: NaN")
    }

    return base ** power
}