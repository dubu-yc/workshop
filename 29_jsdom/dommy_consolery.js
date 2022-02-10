/*
    Team RiftHerald :: Josephine Lee, Yoonah Chang
    SoftDev pd2
    K29: DOMfoolery++
    2022-02-10r
*/

//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

//adds to the list of elements on the HTML page
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

//n is the index
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

//makes all the items red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

var fibitem = document.getElementById("b1");
var facitem = document.getElementById("b2");
var gcditem = document.getElementById("b3");

var fibchange = function() {
  let num = 4;
  console.log(num);
  fibitem.innerHTML = fib(num);
};
var facchange = function() {
  let num = 6;
  console.log(num);
  facitem.innerHTML = fact(num);
};
var gcdchange = function() {
  let num1 = 12;
  let num2 = 18;
  console.log(num1);
  console.log(num2);
  gcditem.innerHTML = gcd(num1, num2);
};

fibitem.addEventListener("click", fibchange);
facitem.addEventListener("click", facchange);
gcditem.addEventListener("click", gcdchange);


//fact, fib, and gcd functions
function fact (n){
    if (n == 0){
      return 1;
    }
    return (n * (fact(n-1)));
}

function fib (n){
    if (n <= 1){
        return n;
    }
    return (fib(n-1) + fib(n-2));
}

function gcd (a, b) {
    let c = min(a, b);
    for (var i = c; i > 0; i--) {
        if (a % i == 0 && b % i == 0) {
            return i;
        }
    }
}

function min (a, b) {
    if (a > b) {
        return b;
    } else {
        return a;
    }
}

//use document.getElementById() to communicate between HTML and JS
var fact5 = document.getElementById("fact");
fact5.innerHTML = "5! = " + fact(5);
var fib5 = document.getElementById("fib");
fib5.innerHTML = "The 5th element of the Fibonacci sequence is " + fib(5);
var gcd10 = document.getElementById("gcd");
gcd10.innerHTML = "The GCD of 12 and 18 is " + gcd(12, 18);