const song_title = document.querySelector('.song-title')
const artist = document.querySelector('.artist')
const music_img = document.querySelector('.music_img')
const lyrics = document.querySelector('.lyricstxt')
const vocab = document.querySelector('.vocabtxt')
const example = document.querySelector('.exampletxt')


// initilize music indexing
let musicIndex = 0

//get music document from backend 
const musics = JSON.parse(document.getElementById('musics').textContent)

// loading a set detail of music in UI
const setSRC = () => {

    // player.src = `/media/${musics[musicIndex].audio_file}`
    song_title.textContent = musics[musicIndex].title
    artist.textContent = musics[musicIndex].artist
    music_img.setAttribute('src', `/media/${musics[musicIndex].cover_image}`)
    lyrics.textContent = musics[musicIndex].lyrics || "No available lyrics"
    vocab.textContent = musics[musicIndex].vocabulary
    example.textContent = musics[musicIndex].example

}

// load first music
setSRC();

document.addEventListener('DOMContentLoaded', function () {
    const listContainer = document.querySelector('.list')
    const exampleText = document.querySelector('.exampletxt')
  
    listContainer.addEventListener('click', function (event) {
      const clickedElement = event.target.closest('.song')
      if (clickedElement) {
        const songIndex = Array.from(clickedElement.parentNode.children).indexOf(clickedElement)
        const selectedSong = musics[songIndex]
        console.log('Selected song:', selectedSong) // Debugging line
        if (selectedSong.example) {
          exampleText.textContent = selectedSong.example
        } else {
          exampleText.textContent = 'No example available for this song.'
        }
      }
    })
  })
