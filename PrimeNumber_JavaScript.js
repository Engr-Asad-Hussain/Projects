var number = parseInt(prompt("Enter a Number?"));

if (number % 2 == 0 || number % 3 == 0)  {
    if (number == 2 || number == 3)  {
        console.log("This is a Prime Number");
        console.log("Number = " + number);
    }
    else {
        console.log("This is not a Prime Number");
        console.log("Number = " + number);
    }
}
else {
    console.log("This is a Prime Number");
    console.log("Number = " + number);
}
