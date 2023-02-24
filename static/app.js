
let totalScore = 0
let wordsPlayed = 0
let gameStatus = ""

// how to toggle classes
// how to detect the game is over if I include timer
// (right now I am doing a button)

$("#boggle-button").on("click", async function(event) {
    event.preventDefault()
    // console.log("You clicked the Boggle Button");
    // console.log("Form value is, ", $('#guess').val())
    let guessedWord = $('#guess').val() 
    let result = await getWord(guessedWord)
    console.log(result.data['result'])
    let wordStatus = result.data['result']

    $('#word-status').removeClass('invisible')

    if (wordStatus === "ok") {
      $('#word-status').addClass('text-success')
      $('#word-status').text(`${guessedWord} is a valid word!`)
      totalScore = totalScore + guessedWord.length
      $('#total-score').text("Total Score: " + totalScore.toString())
    }
    
    if (wordStatus === "not-word") {
      $('#word-status').addClass('text-danger')
      $('#word-status').text(`${guessedWord} is not a word!`)
    }
    
    if (wordStatus === "not-on-board") {
      $('#word-status').addClass('text-danger')
      $('#word-status').text(`${guessedWord} is not on the board!`)
    }
    
    $('#guess').val("")
    wordsPlayed += 1
    $('#words-played').text("Words Played: " + wordsPlayed.toString())

  });

async function getWord(word) {
  const response = await axios.post('http://127.0.0.1:5000/check', {word: word})
  // console.log(response)
  return response
  }

function timer() {

  $("<div class='container'><h3>Countdown: <span id='countdown'></span></h2></div>").appendTo('body')

  let setTimer = new Date().getTime() + 60000;
  let x = setInterval(function () {

    let now = new Date().getTime();
    let distance = setTimer - now;
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);
    $("#countdown").text(seconds + " seconds left!");

    // If the count down is finished, write some text
    if (distance < 0) {
      clearInterval(x);
      $("#guess").addClass("invisible")
      $("#boggle-button").addClass("invisible")
    }
  }, 1000);
}


  