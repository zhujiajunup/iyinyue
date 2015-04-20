/**
 * Created by Administrator on 2015/4/11 0011.
 */
$(function () {
    $('#login').bind("click",function(){
        $.ajax({
            url:"http://127.0.0.1:8000/user/login/",
            type:"POST",
            data:{
                user_name: $('#user_name').val(),
                user_password: $('#user_password').val()
            },
            success: function(data){
                if(data == 1){
                    $.cookie("UserName", $('#user_name').val(), {path:'/'});
                    window.location.href="http://127.0.0.1:8000/index/";
                }
            }
        })
    });
});