function f1(x) {
  return Math.pow(x, 3) - 3 * x + 1;
}
function f2(x) {
  return 2 * Math.pow(x, 3) - 3 * Math.pow(x, 2) - 2 * x + 3;
}
function BisectionMethod(a, b, f, e) {
  // Test  for assumptions.
  let x1 = f(a);
  let x2 = f(b);
  const table = [];
  let c;
  let n = 0;
  // temporary vars to hold the intervals a and b.
  let t_a = a;
  let t_b = b;
  let Error = (t_b - t_a) / 2;
  if (x1 * x2 < 0) {
    while (Error > e) {
      n += 1;
      c = (t_a + t_b) / 2;
      let x3 = f(c);
      Error = (t_b - t_a) / 2;
      // Print the calculation.
      table.push({
        a: t_a,
        b: t_b,
        "c=(a+b)/2": c,
        "f(c)": x3,
        "(b-a)/2": Error,
      });
      // Determine New Interval
      if (x3 * x1 < 0) {
        x2 = x3;
        t_b = c;
      }
      if (x3 * x2 < 0) {
        x1 = x3;
        t_a = c;
      }
      // If we have gotten the roots break out of loop.
      if (x1 === 0 || x2 === 0) break;
    }
    console.table(table);
  } else {
    console.log(
      "Assumptions are not satisfied\nBisection method can not be used"
    );
  }
}
BisectionMethod(0,1, f1, 0.05);
BisectionMethod(1.4, 1.7, f2, 0.00001 );
