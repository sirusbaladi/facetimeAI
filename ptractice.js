console.log('Hello')
var fs = require("fs");
fs.readFile("./gpt.txt", function(text){
    var textByLine = text.split("\n")
})

console.log(textByLine)