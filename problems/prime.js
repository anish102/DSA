let prime = (x) => {
  for (let i = 2; i < x; i++) {
    if (x % i === 0) {
      return false;
    }
  }
  return true;
};

let lst = [];
let a = 2;
let count = 0;
while (count < 50) {
  if (prime(a)) {
    lst.push(a);
    count++;
  }
  a++;
}

console.log(lst);
