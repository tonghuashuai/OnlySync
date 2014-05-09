$(document).ready(function(){
    $(".jtico_weixin").css("background","url(/static/img/weixin.png) no-repeat left");
    $(".jtico_weixin").css("background-size","32px 32px");
    $(".jtico_qzone").css("background","url(/static/img/qzone.png) no-repeat left");
    $(".jtico_qzone").css("background-size","32px 32px");

    $(".jtico").css("margin-right","15px");

    $("#btn_home").click(function(){
        window.location.href = "/"
    });
});
