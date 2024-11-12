async function getF1Score() {
    const URL = "http://localhost:5000/anomaly-predict"
    console.log(URL)
    const data = await fetch(URL)
    const f1score = await data.json()
    console.log(f1score)
    const ptxt = document.getElementById("txt-anomaly")
    ptxt.innerText = f1score
}
