/**
 * 登录ajax
 * 发送信息给后端的接口，以进行验证
 * @type {HTMLElement}
 */
var oButton = document.getElementById("email_key");
var oUsernameTip = document.getElementById("username_email_tip");
var oPasswordTip = document.getElementById("password_tip");
var oKeyTip = document.getElementById("key_tip");
oButton.onclick = function () {
    oUsernameTip.innerText = ""
    oPasswordTip.innerText = ""
    oKeyTip.innerText = ""
    var username = document.getElementById("username_email").value;
    if (username == '') {
        oUsernameTip.innerText = "用户名或邮箱为空！";
    } else {
        // 锁定按钮，防止用户恶意调用邮箱接口
        oButton.disabled = true;
        oButton.innerText = "正在发送中...";
        $.ajax({
            url: "/user/get_login_key/",
            type: 'POST',
            data: {
                'username': username,
            },
            success: function (msg) {
                // 解锁按钮
                oButton.disabled = false;
                if (msg == '已发送') {
                    oButton.style.backgroundColor = "red";
                    oButton.innerText = "已发送";
                    oButton.disabled = "true";
                } else {
                    oUsernameTip.innerText = "用户不存在，请注册";
                    oButton.innerText = "获取邮箱密钥";
                }
            }
        })
    }
};