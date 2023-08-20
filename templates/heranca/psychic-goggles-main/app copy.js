


















const b1 = document.querySelector("#b1");
const b2 = document.querySelector("#b2");
let marginIncrement = -20;

b1.addEventListener("click", function() {
    const slide1 = document.querySelector('.s1');
    marginIncrement -= 20;
    marginIncrement = Math.max(marginIncrement, -80); // Limite de -80%
    slide1.style.marginLeft = `${marginIncrement}%`;
});

b2.addEventListener("click", function() {
    const slide1 = document.querySelector('.s1');
    marginIncrement += 20;
    marginIncrement = Math.min(marginIncrement, 0); // Limite de 0%
    slide1.style.marginLeft = `${marginIncrement}%`;
});






