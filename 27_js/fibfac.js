// Team InvasionOfPrivacy :: Yoonah Chang, William Chen
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-06
// --------------------------------------------------

var fact = function(n) {
if(n < 1){
   return 1
   }
   return n * fact(n-1);
};

var fib = function(n) {
  if(n < 2){
    return n;
  }
  return fib(n - 1) + fib(n - 2);
};

