

        $(document).ready(function () {

            // alert("Привет, Java Script!");
            let valid = true;
            let regExp1 = /^[a-zA-Z][a-zA-Z0-9_\-]{5,15}$/;
            let regExp2 = /^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])[A-Za-z0-9_\-]{8,16}/;
            //let regExp3 = //;

            $('#login').blur( function(){
                let login = $(this).val()
                // Проверка регулярки:
                if (regExp1.test(login)){
                // Проверка занятости логина:
                $.ajax({
                    url:"/account/ajax_reg",
                    data:"login=" + login,
                    success:function(result){
                        if (result.mess == 'занят'){
                            $('#login_img').attr('src','../../static/img/cross.png');
                            $('#login_err').text('Логин занят!');
                            valid = false
                        }else {
                            $('#login_img').attr('src','../../static/img/ok.png');
                            $('#login_err').text('');
                            valid = true
                        }
                    }
                });
                }else{

                    $('#login_img').attr('src','../../static/img/cross.png')
                    $('#login_err').text('Логин должен состоять из букв или цифр(6-16) +(_ / -)!');
                    valid = false
                }
            });
            

            $('#pass1').blur(function){

            });

            $('#pass2').blur(function){

            });
            $('#email').blur(function){

            });

            $('#login').focus(function(){
                $(this).css('border-color','black')
                $('#login_err').text('');
            });
            $('#pass1').focus(function(){
                $(this).css('border-color','black')
                $('#pass1_err').text('');
            });
            $('#pass2').focus(function(){
                $(this).css('border-color','black')
                $('#pass2_err').text('');
            });
            $('#email').focus(function(){
                $(this).css('border-color','black')
                $('#email_err').text('');
            });

            // Код проверки результатов валидации
            $('#submit').click(function(){
                if (valid == true){
                    $('#form1').attr('onsabmit','return true') // - разблокироват отправку на сервер
                }else{
                    $('#form1').attr('onsabmit','return false') // - заблокировать отправку на сервер
                }
            })
        });

