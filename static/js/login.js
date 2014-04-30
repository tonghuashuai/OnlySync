$("#btn_login").click(function(){
    var email = $("#email").val();
    var pwd = $("#pwd").val();
    var next_url = $("#next_url").val();
    $.post("/login", {"email": email, "pwd": pwd, "next_url": next_url}, function(data){
        if (data != ""){
            window.location.href = data;
        }
    });
});
