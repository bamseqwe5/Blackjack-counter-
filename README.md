let runningCount = 0;
let cardsSeen = 0;
let decks = 6;

function scan() {
  navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
    const video = document.getElementById('video');
    video.srcObject = stream;
    // Här kan vi lägga till bildigenkänning om du vill senare!
    alert("Skanning igång (testläge). Lägg till OpenCV.js för riktig analys.");
  });
}
