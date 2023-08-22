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

