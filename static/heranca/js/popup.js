
document.addEventListener("DOMContentLoaded", function() {
    
    alert('{% if error_message %}lá{% endif %}')


    const emailField = document.getElementById("id_email");
    if (emailField) {
        emailField.required = true;
    }
    
    const modalBackground = document.getElementById("modalBackground");
    const modalContent = document.getElementById("modalContent");
    const fecharModalButton = document.getElementById("fecharModalButton");
    const abrirMenuLogin = document.getElementById("menu-login");
    const loginSection = document.getElementById("loginSection");
    const abrirLogin = document.getElementById("abrirLogin");
    const cadastroSection = document.getElementById("cadastroSection");
    const abrirCadastro = document.getElementById("abrirCadastro");

    abrirMenuLogin.addEventListener("click", function () {
        modalBackground.style.display = "flex";
        modalContent.style.display = "block";
        loginSection.style.display = "block";
        cadastroSection.style.display = "none";

    });


    abrirLogin.addEventListener("click", function () {
        modalBackground.style.display = "flex";
        modalContent.style.display = "block";
        loginSection.style.display = "block";
        cadastroSection.style.display = "none";
        
    });

    abrirCadastro.addEventListener("click", function () {
        modalBackground.style.display = "flex";
        modalContent.style.display = "block";
        loginSection.style.display = "none";
        cadastroSection.style.display = "block";

    });

    abrirLogin.addEventListener("click", function () {
        modalBackground.style.display = "block";
        modalContent.style.display = "block";
        loginSection.style.display = "block";
        cadastroSection.style.display = "none";
        
    });

    fecharModalButton.addEventListener("click", function () {
        modalBackground.style.display = "none";
        modalContent.style.display = "none";
    });

    const signupForm = document.querySelector(".signup-form");
    signupForm.addEventListener('submit', function (event) {
        event.preventDefault();
        
        const formData = new FormData(signupForm);

        fetch(signupForm.getAttribute('action'), {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Aqui você pode executar ações após o cadastro bem-sucedido.
                // Por exemplo, fechar o modal e exibir uma mensagem de sucesso.
                modalBackground.style.display = "none";
                modalContent.style.display = "none";
                // ... Outras ações de sucesso ...
            } else {
                // Aqui você pode mostrar erros ou feedback ao usuário.
            }
        })
        .catch(error => {
            console.error('Erro ao enviar formulário:', error);
        });
    });

    

    const errorMessages = document.getElementById("errorMessages");

    loginForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(loginForm);

        

        try {
            const response = await fetch(loginForm.getAttribute("action"), {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
                },
            });

            const data = await response.text();

            // Encontrar elementos <li> dentro da resposta
            const errorList = data.match(/<li>.*?<\/li>/g);

            if (errorList) {
                // Transformar elementos <li> em mensagens de erro
                const errors = errorList.map(li => li.replace(/<\/?li>/g, ""));
                // Exibir mensagens de erro
                errorMessages.innerHTML = errors.map(error => `<p class="error">${error}</p>`).join("");
            } else {
                errorMessages.innerHTML = ""; // Limpar mensagens de erro anteriores
            }
        } catch (error) {
            console.error("Erro ao enviar formulário:", error);
        }

        fetch("/verify_login/", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Se o login for bem-sucedido, atualize a página ou faça algo necessário
                window.location.reload();
            } else {
                // Se houver erro, exiba a mensagem de erro e abra a tela de login
                document.getElementById("error-message").textContent = data.error_message;
                // Você pode adicionar código aqui para abrir a tela de login
            }
        })
        .catch(error => {
            console.error("Erro na solicitação:", error);
        });

    });


    
});
