var length = prompt("Enter a whole number for the length of your rectangle.");
var width = prompt("Enter a whole number for the width of your rectangle.");
 function perimeter(length, width) {
    return 2*( length + width);
}

document.writeln('The perimeter of your rectangle is ' + perimeter(length, width));
