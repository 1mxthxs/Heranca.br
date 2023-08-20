
var modalBackground = document.getElementById("modalBackground");
var fecharModalButton = document.getElementById("fecharModalButton");




// Cadastra Conta

var modalContent = document.getElementById("modalContent");
var cadastroButton = document.querySelector("#cadastroButton");

// Adiciona um evento de clique ao botão/link de cadastro
cadastroButton.addEventListener("click", function() {
    modalBackground.style.display = "block"; // Exibe o fundo escurecido
    modalContent.style.display = "block"; // Exibe o modal
});

    // Adiciona um evento de clique ao botão de fechar
fecharModalButton.addEventListener("click", function() {
    modalBackground.style.display = "none"; // Esconde o fundo escurecido
    modalContent.style.display = "none"; // Esconde o modal
});





// LOGIN

var login = document.getElementById("login");
var login2 = document.querySelector("#login2");
var modalContent3 = document.getElementById("modalContent3");
var fecharModalButton3 = document.getElementById("fecharModalButton3");

// Adiciona um evento de clique ao botão/link de cadastro
login.addEventListener("click", function() {
    modalBackground.style.display = "block"; // Exibe o fundo escurecido
    modalContent3.style.display = "block"; // Exibe o modal
});
login2.addEventListener("click", function() {
    modalBackground.style.display = "block"; // Exibe o fundo escurecido
    modalContent3.style.display = "block"; // Exibe o modal
});

// Adiciona um evento de clique ao botão de fechar
fecharModalButton3.addEventListener("click", function() {
    modalBackground.style.display = "none"; // Esconde o fundo escurecido
    modalContent3.style.display = "none"; // Esconde o modal
});







// Redefinir a Senhar

var esqueceu = document.getElementById("esqueceu");
var esqueceu2 = document.getElementById("esqueceu2");
var modalContent4 = document.getElementById("modalContent4");
var fecharModalButton4 = document.getElementById("fecharModalButton4");


// Adiciona um evento de clique ao botão/link de cadastro
esqueceu.addEventListener("click", function() {
    modalBackground.style.display = "block"; // Exibe o fundo escurecido
    modalContent4.style.display = "block"; // Exibe o modal
});
// Adiciona um evento de clique ao botão de fechar
fecharModalButton4.addEventListener("click", function() {
    modalBackground.style.display = "none"; // Esconde o fundo escurecido
    modalContent4.style.display = "none"; // Esconde o modal
});

















document.getElementById("searchButton").addEventListener("click", function() {
// Restaurar o destaque azul das palavras encontradas
var elementsToClear = document.querySelectorAll("span[style='color: blue;']");
elementsToClear.forEach(function(element) {
    element.style.color = ""; // ou null
});

performSearch();
});

document.getElementById("searchInput").addEventListener("keyup", function(event) {
// Verifica se a tecla pressionada foi o "Enter" (código 13)
if (event.keyCode === 13) {
    // Realize a pesquisa
    performSearch();
}
});

document.getElementById("clearButton").addEventListener("click", function() {
// Deselecionar o texto no input
document.getElementById("searchInput").value = '';

// Restaurar o destaque azul das palavras encontradas
var elementsToClear = document.querySelectorAll("span[style='color: blue;']");
elementsToClear.forEach(function(element) {
    element.style.color = ""; // ou null
});
});

document.querySelector(".limpar").addEventListener("click", function() {
// Deselecionar o texto no input
document.getElementById("searchInput").value = '';

// Restaurar o destaque azul das palavras encontradas
var elementsToClear = document.querySelectorAll("span[style='color: blue;']");
elementsToClear.forEach(function(element) {
    element.style.color = ""; // ou null
});
});

function performSearch() {
var searchText = document.getElementById("searchInput").value.toLowerCase(); // Converter para minúsculas
var elementsToSearch = document.querySelectorAll(".tit, .tit1, .tit2, .tit3, .tit4, .tit5");
var foundElement = null;
var slide1 = document.querySelector('.s1');
let marginIncrement = 0;

elementsToSearch.forEach(function(element, index) {
    var elementText = element.textContent.toLowerCase();
    if (elementText.includes(searchText)) {
        // Criar uma expressão regular para destacar apenas a palavra pesquisada
        var regex = new RegExp(searchText, 'gi');
        var innerHTML = elementText.replace(regex, function(matched) {
            return '<span style="color: blue;">' + matched + '</span>';
        });
        element.innerHTML = innerHTML;
        foundElement = element;

        // Atualizar a posição do slide com base no índice da classe correspondente
        marginIncrement = -20 * index;
        marginIncrement = Math.max(marginIncrement, -80);
        marginIncrement = Math.min(marginIncrement, 0);
        slide1.style.marginLeft = `${marginIncrement}%`;
    } else {
        // Restaurar o texto original sem destaque
        element.innerHTML = elementText;
    }
});

if (foundElement) {
    // Scroll suavemente até o elemento encontrado
    foundElement.scrollIntoView({ behavior: "smooth" });

    // Centralize o elemento encontrado na janela do navegador
    var windowHeight = window.innerHeight;
    var elementTopOffset = foundElement.getBoundingClientRect().top;
    var scrollOffset = elementTopOffset - (windowHeight / 2);
    window.scrollBy(0, scrollOffset);
}
}
