$("#btn_register").click(function(){
    var email = $("#email").val();
    r = /^.*?@.*?\..*$/
    if (!r.test(email)){
        alert_msg("邮箱格式不正确");
        return false;
    }
    var pwd = $("#pwd").val();
    var name = $("#name").val();
    var sex = $("#sex").val();
    $.post("/register", {"email": email, "pwd": pwd, "name": name, "sex": sex}, function(data){
        if (data.msg == "ok"){
            window.location.href = "/";
        }else{
            alert_msg(data.msg);
        }
    });
});
$("#pwd").keypress(function(event){
    if (event.which == 13){
        $("#btn_login").click();
    }
});


$(".sex").click(function(){
    txt = $(this).text();
    code = $(this).attr("code")
    $("#sex_value").text(txt);
    $("#sex").val(code);
});

$("input").change(function(){
    var email = $("#email").val();
    var pwd = $("#pwd").val();
    var name = $("#name").val();

    if (email != "" && pwd != "" && name != ""){
        $("#btn_register").removeAttr("disabled");
    }
});
