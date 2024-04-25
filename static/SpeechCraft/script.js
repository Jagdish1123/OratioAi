$(document).ready(function(){
    $("a").not("#view-more-btn").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function(){
                window.location.hash = hash;
            });
        }
    });

    $("#view-more-btn").on('click', function(event) {
        event.preventDefault();
        window.location.href = 'converter.html';
    });
});

const output = document.getElementById('output');
const startBtn = document.getElementById('start-btn');
const languageSelect = document.getElementById('language-select');

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
recognition.lang = languageSelect.value;
recognition.interimResults = false;
recognition.maxAlternatives = 1;

startBtn.addEventListener('click', () => {
    startBtn.textContent = 'Listening...';
    recognition.start();
});

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("convertButton").addEventListener("click", function(event) {
        event.preventDefault(); // Prevent default behavior of button click
        console.log("Button clicked!");
    });
});


recognition.addEventListener('result', async (e) => {
    const transcript = Array.from(e.results)
        .map(result => result[0].transcript)
        .join('');

    const selectedLanguage = languageSelect.value;
    const translatedText = await translateText(transcript, selectedLanguage);

    output.textContent = translatedText;
    startBtn.textContent = 'Start Recording';
});

recognition.addEventListener('error', (e) => {
    output.textContent = 'Error occurred: ' + e.error;
    startBtn.textContent = 'Start Recording';
});

function translateText(text, targetLanguage) {
    return new Promise((resolve, reject) => {
        const apiUrl = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=' + targetLanguage + '&dt=t&q=' + encodeURI(text);

        $.ajax({
            url: apiUrl,
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                const translatedText = response[0][0][0];
                resolve(translatedText);
            },
            error: function(xhr, status, error) {
                reject(error);
            }
        });
    });
}

function playAudio() {
    var audio = document.getElementById("audio");
    audio.play();
}
