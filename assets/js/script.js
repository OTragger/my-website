//Oswald HOUNDEKON 2022


//////////////Audio file play-pause
const audioElement = document.getElementById("audio-player");
const playButton = document.getElementById("button-play-pause");
const playicon = document.getElementById("play-pause-icon");

function togglePlay() {
  if (audioElement.paused) {
    audioElement.play();
    playicon.classList.remove("bi-music-note");
    playicon.classList.add("bi-music-note-list");
  } else {
    audioElement.pause();
    playicon.classList.remove("bi-music-note-list");
    playicon.classList.add("bi-music-note");
    
  }
}

playButton.addEventListener("click", togglePlay);





/////////////////////////////////////////////////////// project details page

//next project section 

var parallaxBox = document.querySelector('#next-project');
var nextProjectLink = document.querySelector('#next_project_link');
var previousProjectLink = document.querySelector('#previous_project_link');

const ondown = e =>{
    //check and register mouse position
    parallaxBox.dataset.mouseDownAtX = e.clientX;
    parallaxBox.dataset.mouseDownAtY = e.clientY;
}

const onenter = e =>{
    parallaxBox.dataset.mouseDownAtX = e.clientX;
    parallaxBox.dataset.mouseDownAtY = e.clientY;
}

const onmove = e =>{
    const mouseDeltaX = parseFloat(parallaxBox.dataset.mouseDownAtX) - e.clientX,
    mouseDeltaY = parseFloat(parallaxBox.dataset.mouseDownAtY) - e.clientY,
    maxDeltaX = parallaxBox.clientWidth,
    maxDeltaY = parallaxBox.clientHeight;

    const percentageX = Math.max(Math.min(((mouseDeltaX / maxDeltaX)*100),50),0),
    percentageY = Math.max(Math.min(((mouseDeltaY / maxDeltaY)*100),50),0);
    //console.log('percentage-x: ',percentageX , 'percentage-y: ',percentageY);
    parallaxBox.animate({
        backgroundPosition:`${100 - percentageX-40}% ${100 - percentageY-40}%`
    },{duration:1200, fill:'forwards'});
}


const onup = e =>{
    parallaxBox.dataset.mouseDownAtX = '0';
    parallaxBox.dataset.mouseDownAtY = '0';
}
const onleave = e =>{
    parallaxBox.dataset.mouseDownAtX = '0';
    parallaxBox.dataset.mouseDownAtY = '0';
}

parallaxBox.onmouseenter = e =>onenter(e);
parallaxBox.onmouseleave = e =>onleave(e);

parallaxBox.onmousemove = e =>onmove(e);
parallaxBox.ontouchmove = e =>onmove(e.touches[0]);

parallaxBox.ontouchstart = e =>ondown(e.touches[0]);

parallaxBox.ontouchend = e =>onup(e.touches[0]);








//Project Name animation

const changingLetters = "abcdefghijklmnopqrstuvwxyz";

let interval = null;

document.querySelector('#project-name').onmouseover = event =>{
    let iteration = 0;

    clearInterval(interval);

    interval = setInterval(()=>{
        event.target.innerText = event.target.innerText.split('').map((letter,index)=>{if(index<iteration){return event.target.dataset.name[index];}return changingLetters[Math.floor(Math.random()*26)]}).join('');
        if (iteration >= event.target.dataset.name.length){clearInterval(interval);}
        iteration+=1/3;
    }, 50);
};