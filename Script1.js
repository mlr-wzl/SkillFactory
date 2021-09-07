// JavaScript source code
// Task 1
let b = prompt("Введите число");
let a = +b
console.log(typeof b);
if (a == b) {
    if (a % 2) {
        console.log("Нечетное число")
    }
    else {
        console.log("Четное число")
    }
}
else if (typeof b == NaN) {
    console.log("Вы ошиблись, это NaN")
}
else {
    console.log("Вы точно ошиблись")
}


//Task 2
//let x = type variable; e.g.
let x = undefined;
let result = typeof x;
console.log(result)
switch (result) {
    case "number":
        console.log("Это число");
        break;
    case "string":
        console.log("Это строка");
        break;
    case "boolean":
        console.log("Это логический тип");
        break;
    default:
        console.log("Это черт знает что");
}


// Task 3 

function reverseString(str) {
      return str.split("").reverse().join("");
    }
reverseString("hello"); // olleh

// Task 4
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min; 
}
getRandomInt(0, 100)

// Task 5
var items = [1, 2, 2, 2, 25]
console.log(items.length)
items.forEach(function (item, i, arr) {
    console.log(item);
});


// Task 6
var arr1 = [1, 3, 4, 1, 1, 3, 4, 5];
var resultArr1 = arr1.map(function (item, index, array) {
    if (index == 0) { return true }
    else {
        return item == array[index - 1];
    }
}           )
console.log(resultArr1)
if (resultArr1.includes(false)) {
    console.log("Есть разные элементы")
}
else {
    console.log("Массив одинаковый")
}

// Task 7
var tall = [2, 3, 4, 0];
var counter = [0, 0, 0, 0];
var resultArr2 = tall.map(function (item, index, array) {
    if (item == 0) {
        counter[0]++;
    }
    else if (item % 2) {
        counter[1]++;}
    else if (typeof item != "number")
    { counter[3]++;}
    else {counter[2]++;}
    }
)
console.log("Всего четных чисел:" + counter[2])
console.log("Всего нечетных чисел:" + counter[1])
console.log("Всего нулей:" + counter[0])
console.log("Всего других элементов (не чисел):" + counter[3])

// Task 8
let fruits = new Map([

  ["apple", "green"],

  ["strawberry", "red"],

  ["blueberry", "blue"]

]);
for (let elem of fruits) {
    console.log("Ключ - " + elem[0] + ", Значение - " + elem[1]); // apple, strawberry, blueberry
}