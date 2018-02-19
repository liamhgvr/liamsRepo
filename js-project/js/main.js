$(document).ready(function(){
    console.log("hello Main");
    $('button').click(function(word){
        var $word = $('#q').val();
        userSelect($word);
    });
});