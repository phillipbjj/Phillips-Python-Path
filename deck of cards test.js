var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'];
var arr1 = [];
var arr2 = [];
var arr3 = [];
var arr4 = [];

var one = 'D';
var two = 'H';
var three = 'S';
var four = 'C';

var position = 1;

for (var i = 0; i < arr.length; i++) {
    if (position == 1) {
        x = one;
    } else if (position == 2) {
        x = two;
    } else if (position == 3) {
        x = three;
    } else if (position == 4) {
        x = four;
    }
    arr[position].push(arr[i] * x);
    position += 1;
};

var fr = math.random();
var finalArr = [];
var newArr = [];
var eeArr = [];

for (var i = 0; i <finalArr.length; i++) {
    var fr = math.random
    newArr.push({name: finalArr[i], value: fr});
    eeArr.push(fr);
};

eeArr.sort();
var yyArr = [];

for (var i = 0; i < newArr.length; i++) {
    var index = eeArr.indexOf(newArr[i].value);
    newArr.newPos = index;
};
