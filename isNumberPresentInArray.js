var numbers = [2, 4, 5, 5, 10, 23, 8, 16, 32, 90, 100, 77];

console.log(numbers);

var inputUser = parseInt(prompt("Enter any Number ..."));
isPresent = false;

for (var i=0; i<numbers.length; i++)  {
    if (inputUser == numbers[i])  {
        console.log("The number is present in the Array["+i + "]: Number = "+numbers[i]);
        isPresent = true;
        break;
    }
}
if (!isPresent)  {
    console.log("The number is not present in the Array: Number = "+inputUser);
}
