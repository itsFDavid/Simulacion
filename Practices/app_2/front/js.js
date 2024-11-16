const btnPredict = document.getElementById("predict");
btnPredict.addEventListener("click", (event) => {
  getF1Score(event);
  getPrecision(event);
  getRecall(event);
});

async function getF1Score(event) {
  event.preventDefault();
  const URL = "http://localhost:4000/f1-Score";
  const response = await fetch(URL);
  const data = await response.json();
  console.log(data);
  const f1Score = data.f1Score;
  const f1ScoreElement = document.getElementById("txt-anomaly");
  f1ScoreElement.innerHTML = f1Score;
  const matrix = document.getElementById("matrix");
  matrix.style.display = "grid";
}
async function getPrecision(event) {
  event.preventDefault();
  const URL = "http://localhost:4000/precision-Score";
  const response = await fetch(URL);
  const data = await response.json();
  console.log(data);
  const precision = data.precisionScore;
  const precisionElement = document.getElementById("txt-precision");
  precisionElement.innerHTML = precision;
}
async function getRecall(event) {
  event.preventDefault();
  const URL = "http://localhost:4000/recall-Score";
  const response = await fetch(URL);
  const data = await response.json();
  console.log(data);
  const recall = data.recallScore;
  const recallElement = document.getElementById("txt-recall");
  recallElement.innerHTML = recall;
}

document.addEventListener("reset", () => {
  const f1ScoreElement = document.getElementById("txt-anomaly");
  f1ScoreElement.innerHTML = "";
  const matrix = document.getElementById("matrix");
  matrix.style.display = "none";
  const precisionElement = document.getElementById("txt-precision");
  precisionElement.innerHTML = "";
  const recallElement = document.getElementById("txt-recall");
  recallElement.innerHTML = "";
});
