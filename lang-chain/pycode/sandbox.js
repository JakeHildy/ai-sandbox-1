function calcPi(n) {
  if (n === 0) {
    return 0;
  }

  return 4 * (1 - calcPi(n - 1));
}

console.log(calcPi(10));
