$("#btn_submit").click(function(){
    var obj_arr = new Array();
    $(".access").each(function(){
        var access_token = $(this).attr("access_token");
        var code = $(this).attr("code");
        var open_id = $(this).attr("open_id");
        var expires_in = $(this).attr("expires_in");
        var obj = new Object();
        obj.access_token = access_token;
        obj.code = code;
        obj.expires_in = expires_in; 
        obj.open_id = open_id
        obj_arr.push(obj);
    });

    var msg = $("#txt").val();

    var json = JSON.stringify(obj_arr);
    $.post("/", {"data": json, "msg": msg}, function(){
        
    });
});

$("#login").click(function(){
    window.location.href = "/login"
});

access_count = 0
$(".access").each(function(){
    access_count += 1;
});

$("#btn_submit").attr("disabled", "disabled");

if(access_count == 0 && $(".gray").length> 0){
    $("#txt").attr("disabled", "disabled");
    $(".msg").html("请先 <a href='/setting'>设置授权</a> 后再发状态！");
}

function show_size(event, obj){
    len = obj.val().length;
    $("#size").text(len);

    if (len > 0){
        $("#btn_submit").removeAttr("disabled");
    }else{
        $("#btn_submit").attr("disabled", "disabled");
    }
}
