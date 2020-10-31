let playpause_btn = document.querySelector("#mplayer-play"); 

let next_btn = document.querySelector("#mplayer-next"); 
let prev_btn = document.querySelector("#mplayer-prev");

if(track_list.length == 1){
    next_btn.remove();
    prev_btn.remove();
}


let seek_slider = document.querySelector(".seekbar-current");
let curr_time = document.querySelector(".seekbar-curr-time"); 
let total_duration = document.querySelector(".seekbar-dur-time"); 

let songCover = document.querySelector(".mplayer-cover");
let songTitle = document.querySelector(".mplayer-title");
let songAuthor = document.querySelector(".mplayer-artist");

let track_index = 0;
let isPlaying = false;
let updateTimer;

let curr_track = document.createElement('audio'); 

function zeroPad(num, places){
    return String(num).padStart(places, '0');
}

function loadTrack(track_index) {
    clearInterval(updateTimer); 
    resetValues(); 

    
    curr_track.src = track_list[track_index].path; 
    curr_track.load();

    songCover.getElementsByTagName('img')[0].src = track_list[track_index].coverPhoto;
    songTitle.textContent = track_list[track_index].title;
    songAuthor.textContent = track_list[track_index].author;

    updateTimer = setInterval(updateHead, 1000);

    curr_track.addEventListener("ended", nextTrack); 
}

function resetValues() { 
    curr_time.textContent = "00:00"; 
    total_duration.textContent = "00:00"; 
    seek_slider.style.width = "0%";
}

function playpauseTrack() {
    if (!isPlaying) playTrack(); 
    else pauseTrack(); 
} 

function playTrack() {

    curr_track.play(); 
    isPlaying = true;

    playpause_btn.innerHTML = '<i class="fa fa-pause" id="play-pause"></i>'; 
} 

function pauseTrack() {

    curr_track.pause(); 
    isPlaying = false;

    playpause_btn.innerHTML = '<i class="fa fa-play" id="play-pause"></i>'; 
} 

function nextTrack() {

    if (track_index < track_list.length - 1) 
        track_index += 1; 
    else track_index = 0; 

    loadTrack(track_index); 
    playTrack(); 
} 

function prevTrack() {

    if (track_index > 0) 
        track_index -= 1; 
    else track_index = track_list.length; 

    loadTrack(track_index); 
    playTrack(); 
}

function updateHead(){

    if (!isNaN(curr_track.duration)) { 
        let seekPosition = curr_track.currentTime * (100 / curr_track.duration);
        seek_slider.style.width = `${seekPosition}%`;

        let crTimeMins = Math.floor(curr_track.currentTime / 60);
        let crTimeSecs = Math.floor(curr_track.currentTime - crTimeMins * 60);

        let duTimeMins = Math.floor(curr_track.duration / 60);
        let duTimeSecs = Math.floor(curr_track.duration - duTimeMins * 60);

        curr_time.textContent = `${zeroPad(crTimeMins, 2)}:${zeroPad(crTimeSecs, 2)}`;
        total_duration.textContent = `${zeroPad(duTimeMins, 2)}:${zeroPad(duTimeSecs, 2)}`;

    }
}


loadTrack(track_index);