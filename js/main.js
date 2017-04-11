$(document).ready(function(){
    console.log("hello");
    var $item = "";
    $("button").click(function(){
        $item = $("#q").val();
        console.log($item);
    });
});