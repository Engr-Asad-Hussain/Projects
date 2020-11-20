var num = parseInt(prompt("Enter a Number?"));
var isPrime = true;

for (var i=2; i<num; i++)  {
    if (num % i == 0)  {
        console.log("This is not a Prime Number "+num + ":  i="+i);
        isPrime = false;
        break;
    }
}

if (isPrime)  {
    console.log("This is a Prime Number");
}
