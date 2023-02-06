/**
 * 军火库标签选中的active效果变化
 */

var pathname = window.location.href;
var oHeaderText = document.getElementById("header_text");
// 首部类型选择
var oPT = document.getElementById("PT");
var oWeb = document.getElementById("web");
// 渗透测试
oPT.onclick = function () {
    window.location.href = "/arms/index/PT/hot/";
}
if (pathname.indexOf("PT") != -1) {
    oPT.className = "ant-tabs-tab ant-tabs-tab-active";
    oHeaderText.innerText = "渗透测试";
}
// Web
oWeb.onclick = function () {
    window.location.href = "/arms/index/web/hot/";
}
if (pathname.indexOf("web") != -1) {
    oWeb.className = "ant-tabs-tab ant-tabs-tab-active";
    oHeaderText.innerText = "Web安全";
}

// 最新或者最热的选择
var oHot = document.getElementById("hot");
var oNew = document.getElementById("new");
// 最新
if (pathname.indexOf("new") != -1) {
    oNew.className = "ant-radio-button-wrapper ant-radio-button-wrapper-checked";
}
// 最热
if (pathname.indexOf("hot") != -1) {
    oHot.className = "ant-radio-button-wrapper ant-radio-button-wrapper-checked";
}
oHot.onclick = function () {
    if (pathname.indexOf("new") != -1) {
        changePath = pathname.replace("new", "hot");
        window.location.href = changePath;
    }
}
oNew.onclick = function () {
    if (pathname.indexOf("hot") != -1) {
        changePath = pathname.replace("hot", "new");
        window.location.href = changePath;
    }
}