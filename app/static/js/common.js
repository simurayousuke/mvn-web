// layui.use(['element', 'jquery'], function(){
//     var $ = layui.jquery,element = layui.element();
// 	$('#search-').click(function () { alert('sss') })
// });

var button = document.getElementById('search-');
button.onkeydown = function (e) {
 if(e.keyCode === 13) {
    location.assign('/search/' + button.value);
 }
};