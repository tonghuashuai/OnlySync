sina_html = '<iframe src="/auth/sina" width="580" height="350"/>'
$("#btn_sweibo").fancybox({
    content: sina_html,
    afterClose: function(){
        window.location.reload();
    }
});

renren_html = '<iframe src="/auth/renren" width="580" height="410"/>'
$("#btn_renren").fancybox({
    content: renren_html,
    afterClose: function(){
        window.location.reload();
    }
});

douban_html = '<iframe src="/auth/douban" width="350" height="450"/>'
$("#btn_douban").fancybox({
    content: douban_html,
    afterClose: function(){
        window.location.reload();
    }
});

$(".navbar-nav>.active").addClass("float-r");


$(".btn_unband").click(function(){
    code = $(this).attr("id");
    $.post("/j/unband", {"code": code}, function(){
        window.location.reload();
    });
});
