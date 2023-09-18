function entrar(){
    var sidebar = document.getElementById('sidebar');
    sidebar.style.display = 'block';
    var sidebaroff = document.getElementById('sidebar-off');
    sidebaroff.style.display = 'block';

}
function sair(){
    var sidebar = document.getElementById('sidebar');
    sidebar.style.display = 'none';
    var sidebaroff = document.getElementById('sidebar-off');
    sidebaroff.style.display = 'none';
    
}

document.addEventListener("DOMContentLoaded", function() {

    
   
    var menuBtn = document.getElementById("home-linkstyle-menu");
    var sidebar = document.getElementById("sidebar");
    var sidebarOff = document.getElementById("sidebar-off");

    function toggleSidebar() {
        sidebar.classList.toggle("sidebar-show");
    }

    menuBtn.addEventListener("click", toggleSidebar);
    sidebarOff.addEventListener("click", toggleSidebar);
});

function checkScreenWidth() {
    var sidebar = document.getElementById("sidebar");
    if (window.matchMedia("(min-width: 1018px)").matches && sidebar.classList.contains("sidebar-show")) {
        var sidebar = document.getElementById("sidebar");
        sidebar.style.display = "none";
        sidebar.classList.toggle("sidebar-show");
        document.getElementById('sidebar-off').style.display = "none";

    }
}

window.addEventListener("DOMContentLoaded", checkScreenWidth);
window.addEventListener("resize", checkScreenWidth);