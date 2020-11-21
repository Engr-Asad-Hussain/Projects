var rows = parseInt(prompt("Enter number of rows of Pyramid: "));

for (var i=0; i<=rows; i++)  {
    for (var k=0; k<=(rows - i); k++)  {
        document.write("&nbsp");
    }
    for (var j=0; j<=i; j++)  {
        document.write("* ");
    }
    document.write("<br />");
}
