console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href
modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Você tem certeza que quer começar <b>${name}</b></div>
        <div class="text-muted">
            <ul>
                <li>Dificuldade: <b>${difficulty}</b></li>
                <li>Número de questões: <b>${numQuestions}</b></li>
                <li>Pontuação para passar: <b>${scoreToPass}</b></li>
                <li>Tempo: <b>${time}</b></li>
            </ul>
        </div>
    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))