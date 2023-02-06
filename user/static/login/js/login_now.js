/**
 * 登录验证
 */

var oLoginButton = document.getElementById("login");
var oPsswordTip = document.getElementById("password_tip");
var oUsernameTip = document.getElementById("username_email_tip");
var oKeyTip = document.getElementById("key_tip");
oLoginButton.onclick = function () {
    oUsernameTip.innerText = ""
    oPasswordTip.innerText = ""
    oKeyTip.innerText = ""
    var username = document.getElementById("username_email").value;
    var password = document.getElementById("password").value;
    var vercode = document.getElementById("vercode").value;
    $.ajax({
        url: "/user/login_now/", type: 'POST', data: {
            'username': username, 'password': password, 'vercode': vercode,
        }, success: function (msg) {
            console.log(msg)
            if (msg == '用户名或密码或邮箱密钥错误') {
                oPsswordTip.innerText = "用户名或密码或邮箱密钥错误";
            } else if (msg == '提交的信息过长，被后端拦截') {
                oPsswordTip.innerText = "提交的信息过长，被后端拦截";
            } else {
                window.location.href = "/";
            }
        }
    });
}