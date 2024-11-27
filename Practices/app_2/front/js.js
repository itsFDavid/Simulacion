const URL = "http://localhost:4000";
const responseTxt = document.getElementById("responseTxt");

const btnPredict = document.getElementById("predict");
btnPredict.addEventListener("click", async (event) => {
  await getF1Score(event);
  await getPrecision(event);
  await getRecall(event);
});

async function getF1Score(event) {
  event.preventDefault();
  let url = URL + "/f1-Score";
  const response = await fetch(url);
  const data = await response.json();
  const f1Score = data.f1Score;
  const f1ScoreElement = document.getElementById("txt-anomaly");
  f1ScoreElement.innerHTML = f1Score;
  const matrix = document.getElementById("matrix");
  matrix.style.display = "grid";
}
async function getPrecision(event) {
  event.preventDefault();
  let url = URL + "/precision-Score";
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
  const precision = data.precisionScore;
  const precisionElement = document.getElementById("txt-precision");
  precisionElement.innerHTML = precision;
}
async function getRecall(event) {
  event.preventDefault();
  const url = URL + "/recall-Score";
  const response = await fetch(url);
  const data = await response.json();
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
