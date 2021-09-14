// JavaScript source code

// Task 1
function countValues(array) {
    //var tall = [2, 3, 4, 0];
    var counter = [0, 0, 0, 0];
    var resultArr2 = array.map(function (item, index, array) {
        if (item == 0) {
            counter[0]++;
        }
        else if (item % 2) {
            counter[1]++;
        }
        else if (typeof item != "number")
        { counter[3]++; }
        else { counter[2]++; }
    }
    )
    console.log("Всего четных чисел:" + counter[2])
    console.log("Всего нечетных чисел:" + counter[1])
    console.log("Всего нулей:" + counter[0])
    console.log("Всего других элементов (не чисел):" + counter[3])
}
array1 = [2, 3, 4, 0];
countValues(array1)

// Task 2
function simpleValue(n) {
    if (n == 0 || n == 1) {
        console.log("Оставьте в покое 0 и 1, введите другое число")
        return false
    }
    if (n > 1000) {
        console.log("Введите число меньше 1000")
        return false
    }
    
    for (let j = 2; j < n; j++) { // проверить, делится ли число..
        if (n % j == 0) {
            return "число не простое";
        }  // не подходит, берём следующее

        else {
            continue
        }
    }
    return "число простое"
}
simpleValue(7)

// Task 3
function func1(a) {
  return function func2(b) {
              return a + b;
      }
}
const result = func1(7)(3);
console.log(result);

// Task 4
a = prompt("Введите первое число");
b = prompt("Введите второе число, больше первого");
const intervalId = setInterval(function () {
    console.log(a);
    a++;
    if (a > b) {
        clearInterval(intervalId)
                }
    }
        , 1000);

// Task 5
const fatBodyArrowFunction = (x, n) => {

    const result = Math.pow(x,n);

    return result;

};
fatBodyArrowFunction(5,2)

