/**
 * 注册验证
 */

var oRegisterButton = document.getElementById("register");
var oPsswordTip = document.getElementById("password_tip");
var oEmailTip = document.getElementById("email_tip");
var oUsernameTip = document.getElementById('username_tip');
var oKeyTip = document.getElementById('key_tip');
oRegisterButton.onclick = function () {
    oUsernameTip.innerText = "";
    oPsswordTip.innerText = "";
    oKeyTip.innerText = "";
    oEmailTip.innerText = "";
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var vercode = document.getElementById("vercode").value;
    var email = document.getElementById("email").value;
    $.ajax({
        url: "/user/register_now/",
        type: 'POST',
        data: {
            'username': username,
            'password': password,
            'email': email,
            'vercode': vercode,
        },
        success: function (msg) {
            if (msg == '提交的信息过长，被后端拦截') {
                oUsernameTip.innerText = "提交的信息过长，被后端拦截";
            } else if (msg == '用户名已存在') {
                oUsernameTip.innerText = "用户名已存在";
            } else if (msg == '密码请包含大写字母、小写字母、特殊符号、数字中的任意三项') {
                oPsswordTip.innerText = "密码请包含大写字母、小写字母、特殊符号、数字中的任意三项";
            } else if (msg == '邮箱密钥错误') {
                oKeyTip.innerText = "邮箱密钥错误";
            } else {
                window.location.href = "/";
            }
        }
    });
}