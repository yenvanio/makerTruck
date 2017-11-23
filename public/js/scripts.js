$(document).on('click', '.nav-link', function(e) {
    $('.nav-item').find(".active").removeClass("active");
    $(this).parent().addClass('active');
});​

// $(".nav-link").on("click", function(){
//    $(".nav-item").find(".active").removeClass("active");
//    $(this).parent().addClass("active");
// });
