/**
 * 注册ajax
 * 发送信息给后端的接口，以进行验证
 * @type {HTMLElement}
 */
var oButton = document.getElementById("email_key");
var oPsswordTip = document.getElementById("password_tip");
var oUsernameTip = document.getElementById("username_tip");
var oEmailTip = document.getElementById("email_tip");
var oKeyTip = document.getElementById('key_tip');
oButton.onclick = function () {
    oUsernameTip.innerText = "";
    oPsswordTip.innerText = "";
    oKeyTip.innerText = "";
    oEmailTip.innerText = "";
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    if (username == '') {
        oUsernameTip.innerText = "用户名为空！";
    } else if (email == '') {
        oEmailTip.innerText = "邮箱为空！";
    } else {
        // 锁定按钮，防止用户恶意调用邮箱接口
        oButton.disabled = true;
        oButton.innerText = "正在发送中...";
        $.ajax({
            url: "/user/get_register_key/",
            type: 'POST',
            data: {
                'username': username,
                'email': email,
            },
            success: function (msg) {
                // 解锁按钮
                oButton.disabled = false;
                if (msg == '已发送') {
                    oButton.style.backgroundColor = "red";
                    oButton.innerText = "已发送";
                    oButton.disabled = true;
                } else if (msg == '用户名已存在') {
                    oUsernameTip.innerText = "用户名已存在";
                    oButton.innerText = "获取邮箱密钥";
                } else if (msg == '邮箱已被注册') {
                    oEmailTip.innerText = "邮箱已被注册";
                    oButton.innerText = "获取邮箱密钥";
                } else {
                    oEmailTip.innerText = "邮箱格式有误";
                    oButton.innerText = "获取邮箱密钥";
                }
            }
        })
    }
};