const { getAllPhasesAndProblems } = require('./lib/dsa-scanner.js');

try {
  const { problems } = getAllPhasesAndProblems();
  console.log("Total Problems scanned:", problems.length);
  const first = problems[0];
  console.log("Problem:", first.title);
  console.log("Brute Code length:", first.bruteCode.length);
  console.log("Optimal Code length:", first.optimalCode.length);
  console.log("Optimal Code Preview:\n", first.optimalCode.slice(0, 150));
} catch (e) {
  console.error("Error running test:", e);
}
