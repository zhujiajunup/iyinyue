/**
 * Created by Administrator on 2015/4/9 0009.
 */

$(function () {
    $('#register').bind("click",function(){
        $.ajax({
            url:"http://127.0.0.1:8000/user/register/",
            type:"POST",
            data:{
                user_name: $('#user_name').val(),
                user_email: $('#user_email').val(),
                user_password: $('#user_password').val()
            },
            success: function(data){
                if(data == 1){
                    window.location.href="http://127.0.0.1:8000/index/";
                }
            }
        })
    });
});