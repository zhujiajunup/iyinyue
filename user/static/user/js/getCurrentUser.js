/**
 * Created by Administrator on 2015/4/11 0011.
 */
$(function () {
    var value = $.cookie("UserName") == undefined ;
    if(value){
        window.location.href = 'http://127.0.0.1:8000/user/login/';
    }else{
        var user_info = '' ;
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/user/getUserInfo/?user_name='+$.cookie("UserName"),
            dateType:'json',
            contentType:"application/json",
            async:false,
            success: function(data){
                user_info = data
            }
        });

        $('.dropdown .bg').append(
            '<span class="thumb-sm avatar pull-right m-t-n-sm m-b-n-sm m-l-sm">'+
            '                <img src="/static/iyinyue/images/a0.png" alt="...">'+
            '              </span>'+ user_info['user_name']+
            '               <b class="caret"></b>'+
            '            </a>'
        )
    }
});