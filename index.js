import './streaming-client-api.js';

// Get the local video stream
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    const localVideo = document.getElementById('local-video');
    localVideo.srcObject = stream;
  })
  .catch(error => console.error('Error accessing media devices.', error));

function addStream(stream) {
const talkVideo = document.getElementById('local-video');
talkVideo.srcObject = stream;

// update the CSS of the video element
talkVideo.style.width = '100%';
talkVideo.style.height = '100%';
talkVideo.style.objectFit = 'cover';
}
  