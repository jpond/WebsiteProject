function stickyTopBar() {
    var navbar = document.getElementById("header_links");
    var sticky = navbar.offsetTop;
    if(window.pageYOffset >= sticky){
        navbar.classList.add("sticky");
    } else{
        navbar.classList.remove("sticky");
    }
}