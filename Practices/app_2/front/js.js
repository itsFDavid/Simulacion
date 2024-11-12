const btnPredict = document.getElementById("predict")
btnPredict.addEventListener("click", getF1Score)

async function getF1Score(event) {
    event.preventDefault()
    const URL = "http://localhost:4000/anomaly-predict"
    const response = await fetch(URL)
    const data = await response.json()
    console.log(data)
    const f1Score = data.f1Score 
    const f1ScoreElement = document.getElementById("txt-anomaly")
    f1ScoreElement.innerHTML = f1Score
    const matrix = document.getElementById("matrix")
    matrix.style.display = "flex"
}

document.addEventListener("reset", () => {
    const f1ScoreElement = document.getElementById("txt-anomaly")
    f1ScoreElement.innerHTML = ""
    const matrix = document.getElementById("matrix")
    matrix.style.display = "none"
});
