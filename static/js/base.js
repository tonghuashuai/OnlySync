$(".nav_li").each(function(){
    url = location.pathname;
    if ($(this).children("a").attr("href") == url){
        $(this).attr("class", "nav_li active")
    }
});

function show_loading(){
        html = '<div class="loading">\
        <div class="rect1"></div>\
        <div class="rect2"></div>\
        <div class="rect3"></div>\
        <div class="rect4"></div>\
        <div class="rect5"></div>\
    </div>'
    $("#loading").html(html);
}

function close_loading(){
    $("#loading").html('');
}
