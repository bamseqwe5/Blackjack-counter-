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
{
  "name": "Blackjack Counter",
  "short_name": "CardCounter",
  "start_url": "index.html",
  "display": "standalone",
  "background_color": "#000000",
  "description": "Counts cards in blackjack using camera",
  "icons": []
}
