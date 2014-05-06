html = "<iframe src='/auth/sina' width='580' height='350'/>"


$("#btn_sweibo").fancybox({
    content: html,
    afterClose: function(){
        window.location.reload();
    }
});

$(".navbar-nav>.active").addClass("float-r");
