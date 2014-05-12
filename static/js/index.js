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
        window.location.href = "/share?txt=" + msg;
    });
});

$("#login").click(function(){
    window.location.href = "/login";
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
    var len = obj.val().length;
    $("#size").text(len);

    if (len > 0){
        $("#btn_submit").removeAttr("disabled");
    }else{
        $("#btn_submit").attr("disabled", "disabled");
    }
}

function getLocation(){
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showPosition);
    }else{
        alert("不支持定位");
    }
}
function showPosition(position)
{
    var lat = position.coords.latitude; 
    var lng = position.coords.longitude;  
    var url = "http://api.map.baidu.com/geocoder/v2/?ak=gQK596QPc93W9DGbrxRrqilA&callback=renderReverse&location=" + lat + "," + lng + "&output=json&pois=1";
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;
    document.body.appendChild(script);
}
function renderReverse(response){
    var html = "<div class='list-group'>";
    var i = 0;
    var pois = response.result.pois;
    for (i = 0; i < pois.length; i++){
        html +=  "<a href='javascript: void(0);' class='list-group-item'>" + pois[i].name + "</a>";
    }
    html += "</div>";
    $.fancybox({
        content: html,
        afterShow:function(){
            $(".list-group-item").click(function(){
                var name = $(this).text();
                var short_name = name;
                if (name.length > 10){
                    short_name = name.substring(0, 10) + " ...";
                }
                $("#btn_locate").text(short_name); 
                $("#btn_locate").attr("name", name); 
                $.fancybox.close();
            });
        }
    });
}

$("#btn_locate").click(function(){
    var name = $(this).attr("name");
    if (name == ""){
        $(this).text("正在定位 ...");
        getLocation();
    }else{
        $(this).text("定个位");
        $(this).attr("name", "");
    }
});
