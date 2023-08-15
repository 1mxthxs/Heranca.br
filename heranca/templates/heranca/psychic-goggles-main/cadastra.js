let nome = document.querySelector('#nome')
let validnome = false

let email = document.querySelector("#email")
let validemil = false

let senha = document.querySelector("#senha")
let validsenha = false


nome.addEventListener('keyup', ()=> {
    if(nome.value.length <= 1){
        nome.setAttribute('style' , 'color: red')
        validnome = false
    } else{
        validnome = true
        nome.setAttribute('style', 'color: green')
    }
})
email.addEventListener('keyup', ()=> {
    if(email.value.length <= 1){
        email.setAttribute('style' , 'color: red')
        validemil = false
    } else{
        validemil = true
        email.setAttribute('style', 'color: green')
    }
})
senha.addEventListener('keyup', ()=> {
    if(senha.value.length <= 1){
        senha.setAttribute('style' , 'color: red')
        validsenha = false
    } else{
        validsenha = true
        senha.setAttribute('style', 'color: green')
    }
})



function cadastra() {
    if(validnome && validemil && validsenha){
        let listaUser = JSON.parse(localStorage.getItem('listaUser') || '[]')

        listaUser.push(
            {
                nomecad: nome.value,
                emailcad: email.value,
                senhacad: senha.value
            }
        )


        localStorage.setItem('listaUser', JSON.stringify(listaUser))

        alert("Sucesso")
    } else{
        alert("Não foi possivel criar a conta")
    }
}







function Entrar(){
    let logEmail = document.querySelector("#logEmail")
    let logSenha = document.querySelector("#logSenha")

    let listaUser = []

    let userValid = {
        email: '',
        senha: ''
    }

    listaUser = JSON.parse(localStorage.getItem('listaUser'))

    listaUser.forEach((item) => {
        if(logEmail.value == item.emailcad && logSenha.value == item.senhacad){
            userValid = {
                nome: item.nomecad,
                email: item.emailcad,
                senha: item.senhacad
            }

            alert("Logado com Sucesso, Bem vindo " + userValid.nome)
        }
    })
    if(userValid.email == '' || userValid.senha == ''){
        alert("Falhar ao logar")
    }

    console.log(userValid)
}

